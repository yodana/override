# Override level08

On peut voir que le fichier dans la source est ouvert deux fois: une fois sans ./backups et l autre fois avec.
La demarche a suivre est de creer un repertoire dans /tmp pour que le fichier /home/users/level09/.pass soit ecrit dans /backups/home/users/level09/.pass
''' cd tmp
    mkdir backups
    cd backups
    mkdir home
    cd home
    mkdir users
    cd users
    mkdir level09
'''

> ../home/users/level08/level08 home/users/level09/.pass
> cat backups/home/users/level09/.pass
Cela va creer un fichier .pass ou il y aura le flag a l interieur.  