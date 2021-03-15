import os
print("Welcome to my LVM ")
print("1.create LVM\n2.extend partition\n3.Add more device to Volume group")
choice = int(input ("enter ur choice : "))

def create_volume_group():
	print("Listing the devices mounted on this host")
	os.system("fdisk -l")
	storages=input("enter path of storage devices /dev/sda : ").split()
	print("\n")
	for i in storages:
		os.system("pvcreate {}".format(i))
	print("\n")
	vg_name=input("enter name of virtual group : ")
	
	cmd = ''
	for i in storages:
		cmd = cmd + ' ' + i 
		
	os.system("vgcreate {} {}".format(vg_name,cmd))
	print("\n")
	size=input("enter size of partition :")
	name_lvm=input("Enter the name of partition :")
	print("\n")
	os.system("lvcreate --size {}G --name {} {}".format(size,name_lvm,vg_name))
	os.system("mkfs.ext4 /dev/{}/{}".format(vg_name,name_lvm))
	print("\n")
	mount_point=input("Enter the mount point name : ")
	print("\n")
	os.system("mkdir /{}".format(mount_point))
	os.system("mount /dev/{}/{}/{}".format(vg_name,name_lvm,mount_point))
	os.system("mount /dev/{}/{}/{}".format(vg_name,name_lvm,mount_point))


def extend_partition_size():
	size=input("Enter the size ")
	vgname=input("Enter the name of vg group")
	name=input("Name of partition")
	os.system("lvextend --size +{}G /dev/{}/{}".format(size,vgname,name))
	os.system("resize2fs /dev/{}/{}".format(vgname,name))

def extend_volume_group():
	print("List of devices you have :\n")
	os.system("fdisk -l")
	print("\n\n")
	vg_name=input("Enter the name of vg group :# ")
	new_hd=input("Enter new HD device (/dev/sdd.../dev/sdc) :# ")
	os.system("pvcreate {}".format(new_hd))
	os.system("vgextend {} {}".format(vg_name,new_hd))
	print("\nDo you want to extend space of LV(Y/N) : ")
	choice=input("##").capitalize()	
	if(choice=="Y"):
		size=int(input("Enter size to be extended for partition :"))
		name=input("Name of partition :")
		os.system("lvextend --size +{} /dev/{}/{}".format(size,vgname,name))
		os.system("resize2fs /dev/{}/{}".format(vgname,name))
		print("\n")
		print("Size of LV increased! by {}".format(size))
	else:
		print("Volume group extended successfully")
		exit()	
	

if(choice==1):
	create_volume_group()
	print("Done")
elif(choice==2):
	extend_partition_size()
	print("Done")
elif(choice==3):
	extend_volume_group()
	print("Done")
else:
	exit()
	
