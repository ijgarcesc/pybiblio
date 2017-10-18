import sys
import os
import pandas
import pandas as pd
import matplotlib.pyplot as plt
#import argparse



#parser = argparse.ArgumentParser(description='pepito')


#parser.add_argument('-y', action='store_const')

#parser.add_argument('-s', action='store_const', dest='data',
#                    help='displays number of documents from each source')                                        
                    
#print parser.parse_args()


def documents_per_year(csv = False, plot=False):
    """
    Computes the number of documents by year
    
    Args:

        csv (Boolean): Generate CSV file.
        plot (Boolean): Generate JPG file.
    
    Returns:
        Table 
        
    **Example.**
   
    >>> documents_per_year() # doctest: +NORMALIZE_WHITESPACE
              Documents
    Year
    2017       1703
    2018        297
   

    """
    x = data.groupby('Year').size()
    table = pd.DataFrame(x, columns=['Documents'])
    table.index.names = ['Year']    
    if csv == True:
        tables = r'../tables' 
        if not os.path.exists(tables):
           os.makedirs(tables)  
        (table.sort_index(ascending=True)).to_csv('../tables/Documents_per_year.csv')
    if plot is True:
       SP = r'../plots/SP' 
       if not os.path.exists(SP):
          os.makedirs(SP)
       plt.barh(table.index,table['Documents'])
       plt.yticks(table.index)
       plt.ylabel('Año')
       plt.xlabel('Documentos')
       plt.savefig('../plots/SP/Documentos_por_año.jpg')
       EN = r'../plots/EN' 
       if not os.path.exists(EN):
          os.makedirs(EN)
          os.chdir(EN)
       plt.barh(table.index,table['Documents'])
       plt.yticks(table.index)
       plt.ylabel('Year')
       plt.xlabel('Documents')
       plt.savefig('../plots/EN/Documents_per_year.jpg')
    print(table.sort_index(ascending=True))  
       
def documents_per_source(csv = False, plot=True):
    """
    Computes the number of documents in the 10 most recurrent sources.
    If you want to generate a list with the all sources recurrences,
    you must generate the CVS file.
       
    Args:

        csv (Boolean): Generate CSV file.
        plot (Boolean): Generate JPG file.
    
    Returns:
        Table 
        
    **Example.**
   
    >>> documents_per_source() # doctest: +NORMALIZE_WHITESPACE
                                                            Documents
    Source                                                       
    Scientific Reports                                       1082
    Nature Communications                                      78
    Methods in Molecular Biology                               37
    Advances in Intelligent Systems and Computing              32
    Science of the Total Environment                           29
    Journal of Cellular Physiology                             27
    Materials Science and Engineering C                        24
    Biosensors and Bioelectronics                              22
    Journal of the National Cancer Institute                   19
    Cancer Letters                                             18
      
    
    """
    x = data.groupby('Source title').size().sort_values(ascending=False)
    table = pd.DataFrame(x, columns=['Documents'])
    table.index.names = ['Source']
    if csv == True:
       tables = r'../tables' 
       if not os.path.exists(tables):
          os.makedirs(tables)      
       table.to_csv('../tables/Documents_per_source.csv')
    if plot is True:
       SP = r'../plots/SP' 
       if not os.path.exists(SP):
          os.makedirs(SP)
       table1=table[0:10].sort_values('Documents')
       plt.barh(range(len(table1.index)),table1['Documents'])
       plt.yticks(list(range(len(table1.index))),table1.index)
       plt.ylabel('Fuente')
       plt.xlabel('Documentos')
       plt.savefig('../plots/SP/Documentos_por_fuente.jpg')
       EN = r'../plots/EN' 
       if not os.path.exists(EN):
          os.makedirs(EN)
          os.chdir(EN)
       table1=table[0:10].sort_values('Documents')
       plt.barh(range(len(table1.index)),table1['Documents'])
       plt.yticks(list(range(len(table1.index))),table1.index)
       plt.ylabel('Source')
       plt.xlabel('Documents')
       plt.savefig('../plots/EN/Documents_per_source.jpg')
    print(table[0:10])

def documents_per_author(csv = False, plot = True):
    """
    Compute how many times the 10 most recurring authors appear in the documents.
    If you want to generate a list with the all autors recurrences,
    you must generate the CVS file.
       
    Args:

        csv (Boolean): Generate CSV file.
        plot (Boolean): Generate JPG file.
    
    Returns:
        Table 
        
    **Example.**
   
    >>> documents_per_author() # doctest: +NORMALIZE_WHITESPACE
                   Documents
    Authors             
     Wang Y.          56
     Zhang Y.         45
     Li Y.            40
     Wang J.          39
     Li X.            32
     Wang L.          30
     Liu Y.           29
     Zhang J.         26
     Liu Z.           24
     Liu X.           24
      
    
    """
    names=[]
    x = data['Authors'].str.split(',')
    l=len(x)
    for i in range(0,(l-1)):
        names = names + x[i]
    y = pd.DataFrame(names, columns=['Authors'])
    y = y.groupby('Authors').size().sort_values(ascending=False)
    table = pd.DataFrame(y, columns=['Documents'])  
    if csv == True:
       tables = r'../tables' 
       if not os.path.exists(tables):
          os.makedirs(tables)      
       table.to_csv('../tables/Documents_per_author.csv')
    if plot is True:
       SP = r'../plots/SP' 
       if not os.path.exists(SP):
          os.makedirs(SP)
       table1=table[0:10].sort_values('Documents')
       plt.barh(range(len(table1.index)),table1['Documents'])
       plt.yticks(list(range(len(table1.index))),table1.index)
       plt.ylabel('Author')
       plt.xlabel('Documentos')
       plt.savefig('../plots/SP/Documentos_por_autor.jpg')
       EN = r'../plots/EN' 
       if not os.path.exists(EN):
          os.makedirs(EN)
          os.chdir(EN)
       table1=table[0:10].sort_values('Documents')
       plt.barh(range(len(table1.index)),table1['Documents'])
       plt.yticks(list(range(len(table1.index))),table1.index)
       plt.ylabel('Author')
       plt.xlabel('Documents')
       plt.savefig('../plots/EN/Documents_per_author.jpg')
    print(table[0:10])  
    
      
def documents_per_country():
    reg=data['Affiliations']

    table=dict()
    for index, line in enumerate(reg):
        if isinstance(line, str):
            persondata = line.split(';')
            y=set()
            for x in persondata:
                x = x.split()
                y.add(x[-1])
            
            
    #for i in range(0,len(y)):            
    #   table[i]=y[i]
    #  if y[i] not in table:
    #     table.key += 1
    # else:
     #    table.key =1
     #table
    
    return()


def authors_per_year(csv=False):
    year = []
    authors = []
    table = []
    table1 = []
    year = data['Year'].unique()
    authors = data['Authors'].str.split(',')
    l=len(authors)
    for j in year:
        col = []
        for i in range(0,(l-1)):
             if (data.loc[i,'Year'] == j):
                 col=col+authors[i]
                 col.sort()
 #TO DO quitar duplicados de nombres por año o hacer cuenta de nombres         
        table.append(col)
    y=pd.DataFrame(table)
    table1 = y.transpose()
    table1.columns=year
    if csv == True:
       table1.to_csv('Authors_per_year.csv')
    return(table1)
    

def key_words_frecuency(csv=False, plot = False):
     """
    Compute how many times the 10 most recurring authors keywords appear in the documents.
    If you want to generate a list with the all keywords recurrences,
    you must generate the CVS file.
       
    Args:

        csv (Boolean): Generate CSV file.
        plot (Boolean): Generate JPG file.
    
    Returns:
        Table 
        
    **Example.**
   
    key_words_frecuency() # doctest: +NORMALIZE_WHITESPACE
                         
    
    """
    
    table =[]
    table1 = []
    keywords = data['Author Keywords'].str.split(';')
    l=len(keywords)
    for i in range(0,(l)):
        if isinstance(keywords[i],list):
            for j in range(0,len(keywords[i])):
                table.append(keywords[i][j].strip().capitalize())
    frecuency = pd.DataFrame(table, columns=['Keywords'])
    x = frecuency.groupby('Keywords').size().sort_values(ascending=False)
    table1 = pd.DataFrame(x, columns=['Frecuency'])
    table1.index.names = ['Keywords']
    if csv == True:
        tables = r'../tables' 
        if not os.path.exists(tables):
            os.makedirs(tables)      
        table.to_csv('../tables/Key_words_frecuency.csv')
    if plot is True:
       SP = r'../plots/SP' 
       if not os.path.exists(SP):
          os.makedirs(SP)
       table2=table1[0:10].sort_values('Frecuency')
       plt.barh(range(len(table2.index)),table2['Frecuency'])
       plt.yticks(list(range(len(table1.index))),table1.index)
       plt.ylabel('Palabras claves del autor')
       plt.xlabel('Frecuencia')
       plt.savefig('../plots/SP/Frecuencia_palabras_clave.jpg')
       EN = r'../plots/EN' 
       if not os.path.exists(EN):
          os.makedirs(EN)
          os.chdir(EN)
       table2=table1[0:10].sort_values('Frecuency')
       plt.barh(range(len(table2.index)),table2['Frecuency'])
       plt.yticks(list(range(len(table2.index))),table2.index)
       plt.ylabel('Author keywords')
       plt.xlabel('Frecuency')
       plt.savefig('../plots/EN/Key_words_frecuency.jpg')
    print(table1[0:10])
 
    
def documents_per_type(csv = False):
    """
    Computes the number of documents by type
    
       
    Args:

        csv (Boolean): Generate CSV file.
        plot (Boolean): Generate JPG file.
    
    Returns:
        Table 
        
    **Example.**
   
    >>> documents_per_type() # doctest: +NORMALIZE_WHITESPACE
                       Documents
    Document Type               
    Article                 1777
    Review                    91
    Book Chapter              68
    Conference Paper          38
    Conference Review          8
    Letter                     5
    Erratum                    4
    Note                       4
    Editorial                  3
    Short Survey               2
    
    """
    x = data.groupby('Document Type').size().sort_values(ascending=False)
    table = pd.DataFrame(x, columns=['Documents'])
    table.index.names = ['Document Type']    
    if csv == True:
       tables = r'../tables' 
       if not os.path.exists(tables):
          os.makedirs(tables)      
       table.to_csv('../tables/Documents_per_type.csv')
  
    print(table)
 



if __name__ == '__main__':
    ##
   # infilename = sys.argv[1])
    data = pandas.read_table('../data/scopus.csv', sep=',')
    key_words_frecuency(csv=True, plot=True)
    import doctest
    doctest.testmod()  

    ##



