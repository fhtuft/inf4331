


def url_reader(url):
    from urllib import request as urlreq
    import sys   

    text = None
    try: 
            f = urlreq.urlopen(url) #Or somthing with whene
            text = f.readlines()
    except:
        sys.stderr.write("URL bady: " + url + "\n")
    finally:
        if f:
            f.close()
    
    return text




def file_reader(fileName):
    assert fileName.endswith('.csv')
    import csv
    import sqlite3

    with open(fileName,'rb') as f:
        conn = sqlite3.connect(':memory:')
        conn.isolation_level = None
        cur = conn.cursor()
        reader = csv.reader(f)  
        return reader.readLines()
    
    return None  
    


if __name__ == '__main__':
    import sqlite3
    
    conn = sqlite3.connect(':memory:')
    conn.isolation_level = None    
 
    cur = conn.cursor()
    cur.execute("CREATE TABLE temp(year INT,jan FLOAT,feb FLOAT, mar FLOAT,apr FLOAT, may FLOAT,jun FLOAT,jul FLOAT,aug FLOAT,sep FLOAT,okt FLOAT,nov FLOAT,dec FLOAT)")    
    cur.execute("INSERT INTO temp VALUES(1900,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0)");
    cur.execute("INSERT INTO temp VALUES(1901,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0)");
    cur.execute("INSERT INTO temp VALUES(1902,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0)");

    file1 = "./assignment6_files/co2.csv"

    reader = file_reader(file1)

    for lines in reader:
        print(lines)

    url = "http://berkeleyearth.lbl.gov/regions/contiguous-united-states"   

    '''url_data = url_reader(url)
    if url_data:
        print(type(url_data))
        print(url_data)
    '''
    conn.close()
