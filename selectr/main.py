import pandas as pd
import collections
import os
from multiprocessing import Pool

class SelectR:
    """
    SelectR object contains methods to read and parse
    the data from a folder with data in the SelectR format.
    """ 
    
    def __init__(self, folder = None, num_of_processes = 1):
        if folder != None:
            self.folder = folder
            self.files = self.get_files(folder)
            self.df = self.to_df(self.files, num_of_processes)
        
    def get_files(self, folder):
        """
        Finds *.SE1 files in the folder
        
        Parameters
        ----------
        folder : str
            A path containing SE1 files.

        Returns
        -------
        files : list
            A list of files with the SE1 file extension.

        """
        files=[]
        for i in os.listdir(folder):
            file_ext = os.path.splitext(i)[-1]
            if (file_ext == ".SE1") or (file_ext == ".se1"):
                files.append(folder+i)
            
        assert files != [], "no *.SE1 files found"
        return files
        
    def parse(self, file):
        """
        Parses a SE1 file 

        Parameters
        ----------
        file : str
            Name of the file to be parsed.

        Returns
        -------
        list_ : list
            A list of dictionaries containing parsed data.

        """
        list_=[]
        sections={}
        currentsection=''
        with open(file, encoding='utf-8', errors='ignore') as fileObject:
            for line in fileObject:
                line=line.strip()
                if ((line.startswith('[')) and (line.endswith(']'))) or (('*End of Payload*' in line) and (currentsection!='')):
                    if sections!={}:
                        list_.append(sections)
                    else: pass
                    currentsection=line
                    sections={'Section': line.replace('[','').replace(']','').upper()}
                else:
                    if (currentsection!='') and ('=' in line):
                        value=line.split('=')
                        sections[value[0].upper()]=value[-1]
                    else: continue
        return list_
    
    def combine(self, list_, df_list):
        """
        Creates output dataframes organized by section

        Parameters
        ----------
        list_ : list
            A list of dictionaries containing parsed data.

        Returns
        -------
        df_list : list
            A list containing the three seperate dataframes.

        """
        combine=collections.defaultdict(list)
        for i in list_:
            combine[i['Section']].append(i)
        for key in combine:
            df_output=[]
            for j in combine[key]:
                del j['Section']
                df_output.append(pd.DataFrame.from_dict(j, orient='index').transpose())
            df_output=pd.concat(df_output).fillna('N/A')
            df_output.drop_duplicates(list(df_output), inplace=True)
            df_list.append(df_output)
        return df_list

    def to_df(self, SE1_files, num_of_processes = 1):
        """
        Generates dataframes from the SE1 files found in the folder path

        Parameters
        ----------
        SE1_files : list
            A list of the SE1 files to be converted to dataframes.
            
        num_of_processes: natural number
            A natural number representing the amount of the processes the user desires to run

        Returns
        -------
        list_of_dfs : list
            A list of dataframes containing restructured selectR data.

        """
        with Pool(processes = num_of_processes) as pool:
            list_= pool.map(self.parse, SE1_files)
        list_=[x for j in list_ for x in j]
        list_of_dfs=[]
        self.combine(list_, list_of_dfs)
        return list_of_dfs
    