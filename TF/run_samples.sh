for file in exemplos/*
do
    echo $file
    java Parser $file
done
