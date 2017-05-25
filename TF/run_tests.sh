for file in tests/*
do
    echo $file
    java Parser $file
done
