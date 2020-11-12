

"""
Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
:param num_candidate: the number of the candidate
:param file_path: the path to the keyword and hashtag 
files
:param type: type of the keyword, either "keywords" or "hashtags"
:return: (list) a list of string queries that can be done to the search API independently
"""
def get_candidate_queries(num_candidate, file_path):
    try:
        keyword_file_name = 'keywords_candidate_'+str(num_candidate)
        hastag_file_name = 'hastag_candidate_'+str(num_candidate)

        keyword_list = []
        hastag_list = []

        with open(file_path+keyword_file_name+'.txt') as keyword_file:
            keyword_list = list(map(lambda x: x.strip(), keyword_file.readlines()))
            
        with open(file_path+hastag_file_name+'.txt') as hastag_file:
            hastag_list = list(map(lambda x: x.strip(), hastag_file.readlines()))

        return keyword_list+hastag_list
    except IOError:
        print('IOError : wrong path')
    except:
        print("UnknownError : check your code !")

print(get_candidate_queries('num_candidate', 'D:\\Antoine\\Perso\\Ecole\\Ecole d\'ingénieur\\1A\\Coding Weeks\\Week 1\\groupe_9_lunettes_de_vitesse\\data\\candidate_data\\'))
