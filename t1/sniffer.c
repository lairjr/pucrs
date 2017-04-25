#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/ioctl.h>
#include <string.h>
#include <unistd.h>

/* Diretorios: net, netinet, linux contem os includes que descrevem */
/* as estruturas de dados do header dos protocolos                  */

#include <net/if.h>  //estrutura ifr
#include <netinet/ether.h> //header ethernet
#include <netinet/in.h> //definicao de protocolos
#include <arpa/inet.h> //funcoes para manipulacao de enderecos IP

#include <netinet/in_systm.h> //tipos de dados

#define BUFFSIZE 1518

#define HEX01 0x01
#define HEX06 0x06
#define HEX08 0x08
#define HEX11 0x11
#define HEX86 0x86
#define HEX3a 0x3a

// Atencao!! Confira no /usr/include do seu sisop o nome correto
// das estruturas de dados dos protocolos.

unsigned char buff1[BUFFSIZE]; // buffer de recepcao
int sockd;
int on;
struct ifreq ifr;
int ipv6_counter, ipv4_counter, arp_counter, icmp_counter, icmpv6_counter, udp_counter, tcp_counter = 0;

void indentify_package()
{
		if (buff1[13] == HEX06) {
				arp_counter++;
		}
		if (buff1[12] == HEX86) {
				ipv6_counter++;
				if (buff1[20] == HEX3a) {
						icmpv6_counter++;
				}
		} else if (buff1[12] == HEX08) {
				ipv4_counter++;
				if (buff1[23] == HEX11) {
						udp_counter++;
				} else if (buff1[23] == HEX06) {
						tcp_counter++;
				} else if (buff1[23] == HEX01) {
						icmp_counter++;
				}
		}
}

void load_package()
{
		recv(sockd,(char *) &buff1, sizeof(buff1), 0x0);
}

void print_package()
{
		printf("MAC Destino: %x:%x:%x:%x:%x:%x \n", buff1[0],buff1[1],buff1[2],buff1[3],buff1[4],buff1[5]);
		printf("MAC Origem:  %x:%x:%x:%x:%x:%x \n", buff1[6],buff1[7],buff1[8],buff1[9],buff1[10],buff1[11]);
		printf("IP version %x:%x\n", buff1[12], buff1[13]);
		printf("Protocolo %x\n", buff1[22]);
}

void print_summary()
{
		printf("\nTotal packages\n");
		printf("IPv4: %d | IPv6: %d | ARP: %d | ICMP: %d | ICMPv6: %d | UDP: %d | TCP: %d\n",
		       ipv4_counter, ipv6_counter, arp_counter, icmp_counter, icmpv6_counter, udp_counter, tcp_counter);
}

int main(int argc,char *argv[])
{
		/* Criacao do socket. Todos os pacotes devem ser construidos a partir do protocolo Ethernet. */
		/* De um "man" para ver os parametros.*/
		/* htons: converte um short (2-byte) integer para standard network byte order. */
		if((sockd = socket(PF_PACKET, SOCK_RAW, htons(ETH_P_ALL))) < 0) {
				printf("Erro na criacao do socket.\n");
				exit(1);
		}

		// O procedimento abaixo eh utilizado para "setar" a interface em modo promiscuo
		strcpy(ifr.ifr_name, "enp0s3");
		if(ioctl(sockd, SIOCGIFINDEX, &ifr) < 0)
				printf("erro no ioctl!");
		ioctl(sockd, SIOCGIFFLAGS, &ifr);
		ifr.ifr_flags |= IFF_PROMISC;
		ioctl(sockd, SIOCSIFFLAGS, &ifr);

		// recepcao de pacotes
		while (1) {
				load_package();
				print_package();
				indentify_package();
				print_summary();
		}
}
