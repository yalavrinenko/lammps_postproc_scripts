#!/bin/sh

declare -A mount_points=( 
	[desmos]="desmos:/home/yalavrinenko/lammps" 
        [k100]="k100:/home/imorozov/Lavrinenko/nethome/lammps" 
	)

for key in "${!mount_points[@]}"
do
	echo "Mounting ${mount_points[$key]} to $key...."
	sshfs ${mount_points[$key]} $key
	echo "Done."
done
