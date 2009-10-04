# #####################################################################################
#
#  OpenAssembler V3
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2009.06.08
#
# #####################################################################################

import os
try:
	import sys, time,readline
except:
	import sys, time


from Core.Gateway.Gateway import oas_gateway

# #####################################################################################
# this file is for the console loop
# #####################################################################################

class oas_console(oas_gateway):
	def oas_Console(self,imput_to_parse="",mode="normal"):
		
# ###################################################################################
# we are starting a loop and then we are lsitening and sorting out the given commands
# ###################################################################################
		x=1
		while x==1:	
			if imput_to_parse=="":
				try:
					input_command=raw_input ("OpenAssembler--->").strip()
				except KeyboardInterrupt:
					sys.exit()
			else:
				x=0
				input_command=imput_to_parse

			if input_command=="":
				input_command="no character given"

			if input_command=="exit":
				sys.exit(0)

			elif input_command.split()[0]=="list" or input_command.split()[0]=="ls" or input_command.split()[0]=="lc" or input_command.split()[0]=="ln":
				try:
					ltyp=input_command.split()[1]
				except:
					ltyp=""
				if input_command.split()[0]=="ln":
					ltyp="nodetypes"
				elif input_command.split()[0]=="lc":
					ltyp="connections"
				elif input_command.split()[0]=="ls":
					ltyp="scene"
				try:
					src=input_command.split()[2]
				except:
					src=""	
				if mode=="normal":
					self.oas_list(mode=mode,listtype=ltyp,searchtag=src)
				else:
					return  self.oas_list(mode=mode,listtype=ltyp,searchtag=src)
					
			elif input_command.split()[0]=="count":
				try:
					ltyp=input_command.split()[1]
				except:
					ltyp="nodetypes"
				if mode=="normal":
					self.oas_count(mode=mode,counttype=ltyp)
				else:
					return  self.oas_count(mode=mode,counttype=ltyp)			
			
			elif input_command.split()[0]=="create" or input_command.split()[0]=="cr":
				try:
					ndtp=input_command.split()[1]
				except:
					ndtp=""
				if mode=="normal":
					self.oas_create(mode=mode,nodetype=ndtp) 
				else:
					return self.oas_create(mode=mode,nodetype=ndtp) 

			
			elif input_command.split()[0]=="delete" or input_command.split()[0]=="del":
				try:
					ndtp=input_command.split()[1]
				except:
					ndtp="node"	
				try:
					trg=input_command.split()[2]
				except:
					trg=""		
				if mode=="normal":
					self.oas_delete(mode=mode,deletetype=ndtp,target=trg) 
				else:
					return self.oas_delete(mode=mode,deletetype=ndtp,target=trg) 
			
			elif input_command.split()[0]=="rename" or input_command.split()[0]=="rn":
				try:
					old=input_command.split()[1]
				except:
					old="node"	
				try:
					new=input_command.split()[2]
				except:
					new=""		
				if mode=="normal":
					self.oas_rename(mode=mode,old=old,new=new) 
				else:
					return self.oas_rename(mode=mode,old=old,new=new) 			
			
			elif input_command.split()[0]=="show" or input_command.split()[0]=="sh":
				try:
					showtype=input_command.split()[1]
				except:
					showtype=""			
				if mode=="normal":
					self.oas_show(mode=mode,showtype=showtype) 
				else:
					return self.oas_show(mode=mode,showtype=showtype)
									
			elif input_command.split()[0]=="connect" or input_command.split()[0]=="cn":
				try:
					frv=input_command.split()[1]
				except:
					frv=""	
				try:
					tov=input_command.split()[2]
				except:
					tov=""		
				if mode=="normal":
					self.oas_connect(mode=mode,from_variable=frv,to_variable=tov) 
				else:
					return self.oas_connect(mode=mode,from_variable=frv,to_variable=tov)
					 
			elif input_command.split()[0]=="end":
				try:
					endnode=input_command.split()[1]
				except:
					endnode=""			
				if mode=="normal":
					self.oas_end(mode=mode,endnode=endnode) 
				else:
					return self.oas_end(mode=mode,endnode=endnode)
					
			elif input_command.split()[0]=="set":
				try:
					nv=input_command.split()[1]
				except:
					nv=""	
				try:
					vv=input_command.split(" ",2)[2]
				except:
					vv=""		
				if mode=="normal":
					self.oas_set(mode=mode,nodevalue=nv,value=vv) 
				else:
					return self.oas_set(mode=mode,nodevalue=nv,value=vv)
					 
			elif input_command.split()[0]=="framerange":
				try:
					ff=input_command.split()[1]
				except:
					ff=""	
				try:
					ef=input_command.split()[2]
				except:
					ef=""		
				if mode=="normal":
					self.oas_framerange(mode=mode,firstframe=ff,endframe=ef) 
				else:
					return self.oas_framerange(mode=mode,firstframe=ff,endframe=ef)
					
					
			elif input_command.split()[0]=="positions":
				try:
					node=input_command.split()[1]
				except:
					ff=""	
				try:
					px=input_command.split()[2]
				except:
					px=100
				try:
					py=input_command.split()[3]
				except:
					py=100
				if mode=="normal":
					self.oas_positions(mode=mode,nodevalue=node,posx=px,posy=py) 
				else:
					return self.oas_positions(mode=mode,nodevalue=node,posx=px,posy=py)
					 
			elif input_command.split()[0]=="frame":
				try:
					frame=input_command.split()[1]
				except:
					frame=""			
				if mode=="normal":
					self.oas_frame(mode=mode,frame=frame) 
				else:
					return self.oas_frame(mode=mode,frame=frame)

			elif input_command.split()[0]=="run":
				self.oas_run(mode=mode) 

			elif input_command.split()[0]=="generate":
				try:
					fp=input_command.split()[1]
				except:
					print "No filename was given!"
					return
				self.oas_generate(mode=mode,file=fp) 
			
			elif input_command.split()[0]=="new":
				self.oas_new(mode=mode) 
					
			elif input_command.split()[0]=="open":
				try:
					ft=input_command.split()[2]
				except:
					ft=""	
				try:
					fp=input_command.split()[1]
				except:
					fp=""		
				if mode=="normal":
					self.oas_open(mode=mode,filetype=ft,filename=fp) 
				else:
					return self.oas_open(mode=mode,filetype=ft,filename=fp)
					 
			elif input_command.split()[0]=="save":
				if (str(self.oas_save_filename)!="") and (len(input_command.split())<2):
					self.oas_save(mode=mode,filetype=str(self.oas_save_filename)[-3:],filename=str(self.oas_save_filename))
				elif len(input_command.split())>2:
					self.oas_save(mode=mode,filename=input_command.split()[1],filetype=input_command.split()[2])  
										
			elif input_command.split()[0]=="current_file":
				if mode=="normal":
					print self.oas_save_filename
				else:
					return self.oas_save_filename 
			
			elif input_command.split()[0]=="variabletypes":
				if mode=="normal":
					print self.oas_variablecategory
				else:
					rr=[]
					for ks in self.oas_variablecategory.keys():
						rr.append(str(ks)+":"+str(self.oas_variablecategory[ks]['variablecategory']))
					return rr	
			
			elif input_command.split()[0]=="addInput":
				try:
					node=input_command.split()[1]
				except:
					node=""	
				try:
					inputname=input_command.split()[2]
				except:
					inputname=""	
				try:
					variabletype=input_command.split()[3]
				except:
					variabletype=""	
				try:
					defaultvalue=input_command.split()[4]
				except:
					defaultvalue=inputname

				if mode=="normal":
					self.oas_addInput(mode=mode,node=node,variablename=inputname,variabletype=variabletype,defaultvalue=defaultvalue) 
				else:
					return self.oas_addInput(mode=mode,node=node,variablename=inputname,variabletype=variabletype,defaultvalue=defaultvalue)
			elif input_command.split()[0]=="delInput":
				try:
					node=input_command.split()[1]
				except:
					node=""	
				try:
					inputname=input_command.split()[2]
				except:
					inputname=""	

				if mode=="normal":
					self.oas_delInput(mode=mode,node=node,variablename=inputname) 
				else:
					return self.oas_delInput(mode=mode,node=node,variablename=inputname)

			else:
				if input_command!="no character given":
					if mode=="normal":
						print "Command not found. --> "+input_command
