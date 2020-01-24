import numpy as np
import pandas as pd
import pandasql as ps
import sqlite3


def read_sql_queda(queda):

	
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT queda_tesao FROM cable_tabelacondutor
        WHERE secao = '{queda}';
	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()

	
	return read_db


def read_sql_corr(corr):
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT capacidade_conducao FROM cable_tabelacondutor
        WHERE secao = '{corr}';
	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()

	return read_db


def read_sql_dj(dj):
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT dj FROM cable_disjuntor
        WHERE dj = '{dj}';
	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()

	return read_db

def read_sql_filter(projeto):
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT project FROM cable_project
        WHERE id like '{projeto}';

	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()
	
	return read_db


def read_sql_filter_id(id_x):
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT id FROM cable_project
        WHERE project like '{id_x}';

	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()
	
	return read_db

#---
def read_sql_filter_name(id_x):
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT project FROM cable_project
        WHERE id = '{id_x}';

	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()
	
	return read_db

def read_sql_tension(tens):
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT type_tension FROM calc_tension
        WHERE id = '{tens}';
	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()

	return read_db



#--------------------------------------
def table_calc(corrent, tension):
	
	tens = ['1,5','2,5','4','6','10','16','25','35','50','70','95','120','150','185','240','300']
	queda = [34,18,12,7.6,4.5,2.7,1.7,1.2,0.96,0.67,0.48,0.38,0.31,0.25,0.19,0.15]
	corr = [21,30,40,51,71,95,125,155,190,240,290,340,385,440,520,590]

	new = []
	for a in range(len(tens)):
		new.append([tens[a],queda[a],corr[a]])
        

	table = pd.DataFrame(data=new,columns=['Cable','Queda','Corrente'])
	
	result = corrent / tension
	res = round(result + 0.5)

	new = []
	for a in table['Corrente']:
		if res > int(a):
			pass
		else:
			new.append(a)
			num = int(new[0])
	
	new_table = table[table['Corrente'] == num]

	return new_table


def table_tens(p_va, tension):

	tens = ['1,5','2,5','4','6','10','16','25','35','50','70','95','120','150','185','240','300']
	queda = [34,18,12,7.6,4.5,2.7,1.7,1.2,0.96,0.67,0.48,0.38,0.31,0.25,0.19,0.15]
	corr = [21,30,40,51,71,95,125,155,190,240,290,340,385,440,520,590]

	new = []
	for a in range(len(tens)):
		new.append([tens[a],queda[a],corr[a]])
        
	table = pd.DataFrame(data=new,columns=['Cable','Queda','Corrente'])
	
	xx = str(tension)

	result = p_va / int(xx)
	res = round(result + 0.5)

	new = []
	for a in table['Corrente']:
		if res > int(a):
			pass
		else:
			new.append(a)
			num = int(new[0])
	
	new_table = table[table['Corrente'] == num]
	new = []
	for a in new_table['Cable']:
		return a
		#new.append(a)


def table_tens(p_va, tension):

	tens = ['1,5','2,5','4','6','10','16','25','35','50','70','95','120','150','185','240','300']
	queda = [34,18,12,7.6,4.5,2.7,1.7,1.2,0.96,0.67,0.48,0.38,0.31,0.25,0.19,0.15]
	corr = [21,30,40,51,71,95,125,155,190,240,290,340,385,440,520,590]

	new = []
	for a in range(len(tens)):
		new.append([tens[a],queda[a],corr[a]])
        
	table = pd.DataFrame(data=new,columns=['Cable','Queda','Corrente'])
	
	xx = str(tension)

	result = p_va / int(xx)
	res = round(result + 0.5)

	new = []
	for a in table['Corrente']:
		if res > int(a):
			pass
		else:
			new.append(a)
			num = int(new[0])
	
	new_table = table[table['Corrente'] == num]
	new = []
	for a in new_table['Cable']:
		return a
		#new.append(a)

def table_disj(p_va, tens):

	corr = [8,15,18,23,30,38,48,60,68,78,98,123,148,178,228]
	dj = [10,16,20,25,32,40,50,63,70,80,100,125,150,180,200,230]

	new = []
	for a in range(len(corr)):
		new.append([corr[a],dj[a]])
        
	table = pd.DataFrame(data=new,columns=['Corrente','DJ'])
	
	xx = str(tens)

	result = p_va / int(xx)
	res = round(result + 0.5)

	new2 = []
	for a in table['Corrente']:
		if res > int(a):
			pass
		else:
			new2.append(a)
			num = int(new2[0])
	
	new_table = table[table['Corrente'] == num]
	new = []
	for a in new_table['DJ']:
		return a