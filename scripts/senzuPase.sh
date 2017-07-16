# Alexis
# codigoRepo ="https://github.com/alexis05/SenzuAB.git"
folder = "/home/dev1/codigo"
folderDestino = "/var/www/html/Senzu"

echo "borrando codigo..."
cd /home/dev1/codigo
rm /home/dev1/codigo/*

echo "clone.."
git clone https://github.com/alexis05/SenzuAB.git
echo "clone listo"
echo "chmod 777" 
chmod -R 777 /home/dev1/codigo/SenzuAB/

echo "copiando codigo..."
rm -r /var/www/html/Senzu/*
#cd /home/dev1/codigo/SenzuAB/ 
cp -r /home/dev1/codigo/SenzuAB/Senzu/ /var/www/html/
chmod -R 755 /var/www/html/Senzu/
service apache2 restart
