query_insert_data = '''
INSERT INTO peoples(First_Name, Last_Name, Company_Name, Branch) VALUES (?,?,?,?)
'''

query_delete_record = '''
DELETE FROM peoples WHERE id = ?
'''

query_get_all_recs = '''
SELECT * FROM peoples
'''

query_update_recs = '''
UPDATE peoples SET First_Name = ?, Last_Name = ?, Company_Name = ?, Branch = ? WHERE ID = ?
'''
