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

#define IPv6 1
#define IPv4 2
#define ARP 3
#define ICMP 4
#define ICMPv6 5
#define UDP 6
#define TCP 7

// Atencao!! Confira no /usr/include do seu sisop o nome correto
// das estruturas de dados dos protocolos.

typedef struct packet_info {
		int ip_version;
		int protocol;
} packet_info;

unsigned char buff1[BUFFSIZE]; // buffer de recepcao
int sockd;
int on;
struct ifreq ifr;
int ipv6_counter, ipv4_counter, arp_counter, icmp_counter, icmpv6_counter, udp_counter, tcp_counter = 0;

int get_ip_version() {
		if (buff1[12] == HEX86) {
				return IPv6;
		} else if (buff1[12] == HEX08) {
				return IPv4;
		}
		return 0;
}

int get_protocol(int ip_version) {
		switch (ip_version) {
		case IPv4:
				if (buff1[13] == HEX06) {
						return ARP;
				} else if (buff1[23] == HEX11) {
						return UDP;
				} else if (buff1[23] == HEX06) {
						return TCP;
				} else if (buff1[23] == HEX01) {
						return ICMP;
				}

				return 0;
		case IPv6:
				if (buff1[13] == HEX06) {
						return ARP;
				} else if (buff1[20] == HEX3a) {
						return ICMPv6;
				}
				return 0;
		default:
				return 0;
		}
}

packet_info indentify_package()
{
		packet_info info;
		info.ip_version = get_ip_version();
		info.protocol = get_protocol(info.ip_version);

		return info;
}

void accumulate_values(packet_info info)
{
		switch (info.ip_version) {
		case IPv4:
				ipv4_counter++;
				break;
		case IPv6:
				ipv6_counter++;
				break;
		default:
				break;
		}

		switch (info.protocol) {
		case ARP:
				arp_counter++;
				break;
		case ICMP:
				icmp_counter++;
				break;
		case ICMPv6:
				icmpv6_counter++;
				break;
		case UDP:
				udp_counter++;
				break;
		case TCP:
				tcp_counter++;
				break;
		default:
				break;
		}
}

void load_package()
{
		recv(sockd,(char *) &buff1, sizeof(buff1), 0x0);
}

void print_ethernet_header()
{
		printf("---- HEADER ----\n");
		printf("MAC Destino: %x:%x:%x:%x:%x:%x \n", buff1[0],buff1[1],buff1[2],buff1[3],buff1[4],buff1[5]);
		printf("MAC Origem:  %x:%x:%x:%x:%x:%x \n", buff1[6],buff1[7],buff1[8],buff1[9],buff1[10],buff1[11]);
		printf("Tipo: %x:%x\n", buff1[12], buff1[13]);
}

void print_protocol(packet_info info)
{
		if (info.ip_version == 0 || info.protocol == 0)
		{
				printf("Protocolo desconhecido\n");
				return;
		}

		char name[10] = "";
		int buff_position = 0;

		switch (info.protocol) {
		case ARP:
				strncpy(name, "ARP", 6);
				buff_position = 13;
				break;
		case UDP:
				strncpy(name, "UDP", 6);
				buff_position = 23;
				break;
		case ICMP:
				strncpy(name, "ICMP", 6);
				buff_position = 23;
				break;
		case TCP:
				strncpy(name, "TCP", 6);
				buff_position = 23;
				break;
		case ICMPv6:
				strncpy(name, "ICMPv6", 6);
				buff_position = 20;
				break;
		}

		printf("Protocolo: %x (%s)\n", buff1[buff_position], name);
}

void print_arp()
{
		printf("Hardware Address Type: %x %x ()\n", buff1[14], buff1[15]);
		printf("Protocol Address Type: %x %x ()\n", buff1[16], buff1[17]);
		printf("Hardware Address Length: %x\n", buff1[18]);
		printf("Protocol Address Length: %x\n", buff1[19]);
		printf("Operation: %x %x ()\n", buff1[20], buff1[21]);
		printf("Source Hardware Address: %x %x %x %x %x %x ()\n", buff1[22], buff1[23], buff1[24], buff1[25], buff1[26], buff1[27]);
		printf("Source Protocol Address: %x %x %x %x ()\n", buff1[28], buff1[29], buff1[30], buff1[31]);
		printf("Target Hardware Address: %x %x %x %x %x %x ()\n", buff1[32], buff1[33], buff1[34], buff1[35], buff1[36], buff1[37]);
		printf("Target Protocol Address: %x %x %x %x ()\n", buff1[38], buff1[39], buff1[40], buff1[41]);
}

void print_udp()
{
		printf("Source port: %x %x ()\n", buff1[34], buff1[35]);
		printf("Destination port: %x %x ()\n", buff1[36], buff1[37]);
		printf("Length: %x %x ()\n", buff1[38], buff1[39]);
		printf("Checksum: %x %x\n", buff1[40], buff1[41]);
}

void print_tcp()
{
		printf("Source port: %x %x (%d)\n", buff1[34], buff1[35], buff1[34] + buff1[35]);
		printf("Destination port: %x %x ()\n", buff1[36], buff1[37]);
		printf("Seq. Number: %x %x %x %x ()\n", buff1[38], buff1[39], buff1[40], buff1[41]);
		printf("Ack. Number: %x %x %x %x ()\n", buff1[42], buff1[43], buff1[44], buff1[45]);
		printf("Flags: %x %x\n", buff1[46], buff1[47]);
		printf("Window: %x %x\n", buff1[48], buff1[49]);
		printf("Checksum: %x %x\n", buff1[50], buff1[51]);
		printf("Urgent point: %x %x\n", buff1[52], buff1[53]);
}

void print_icmp()
{
		printf("Type: %x ()\n", buff1[34]);
		printf("Code: %x ()\n", buff1[35]);
		printf("Checksum: %x %x\n", buff1[36], buff1[37]);
}

void print_icmpv6()
{
		printf("Type: \n");
		printf("Code: \n");
		printf("Checksum: \n");
}

void print_package_content(int protocol)
{
		if (protocol == 0)
		{
				printf("Corpo de pacote desconhecido\n");
				return;
		}
		printf("---- CORPO DO PACOTE ----\n");
		switch (protocol) {
		case ARP:
				print_arp();
				break;
		case UDP:
				print_udp();
				break;
		case ICMP:
				print_icmp();
				break;
		case TCP:
				print_tcp();
				break;
		case ICMPv6:
				print_icmpv6();
				break;
		}
		printf("---- FIM DO CORPO ----\n");
}

void print_summary()
{
		printf("\nTotal packages\n");
		printf("IPv4: %d | IPv6: %d | ARP: %d | ICMP: %d | ICMPv6: %d | UDP: %d | TCP: %d\n\n",
		       ipv4_counter, ipv6_counter, arp_counter, icmp_counter, icmpv6_counter, udp_counter, tcp_counter);
}

int main(int argc, char *argv[])
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
				print_ethernet_header();
				packet_info info = indentify_package();
				accumulate_values(info);
				print_protocol(info);
				print_package_content(info.protocol);
				print_summary();
		}
}
