
######################################################
# Project: <Juan Miguel Cruz>
# UIN: <655400483>
# repl.it URL: <https://replit.com/@CS111-Fall2021/Project-3-Juan-MiguelMi11#main.py>

# For this project, I received help from the following members of CS111.
# Martin Mitchel, netID 655103220: helped me with some questions and functions
# TA : Tri Quan Do: Helped with question 3 and graphs and formating
# Sandeep Valmiki, netID 654807517: helped with the graphs
# Alex Bernatowicz, netID 664977389: helped with question 4 and 5

######################################################
import csv
import json
import requests
import matplotlib.pyplot as plt
import operator


def get_data_from_file(fn, format=""):
  '''Access the data'''
  lst = []

  # handle the csv file
  if '.csv' in fn or format == 'csv':
    f = open('tax_return_data_2018.csv')
    reader = csv.reader(f)

    for row in reader:
      lst.append(row)

    f.close()

    return lst
    
  # elif json, handle json file
  elif '.json' in fn or format == 'json':
    f = open('states_titlecase.json', "r")
    text = f.read()
    data = json.loads(text)
    
    return data


def get_data_from_internet(url, format = ''):
  '''Access the data from the internet using the url'''
  r = requests.get(url)
  ###IF DATA IS JSON###
  if format == 'json':
    reader = r.json()
    data = []
    for row in reader:
      data.append (row)

  ###IF DATA IS CSV###
  elif format == 'csv':
    reader = csv.reader(r)
    data = []
    for row in reader:
      data.append (row)

  return data

def get_index_for_column_label(header_row, column_label):
  index = header_row.index(column_label)

  return index

def get_state_name(state_names, state_code):
  '''Access the state names'''
  state = ''
  for key in state_names:
    if key['abbreviation'] == state_code:
      state = key ['name']

  return state

def get_state_population(state_populations, state_name):
  '''access the state population '''
  state_name = '.' + state_name
  state_key = ""

  for state_data in state_populations:
    for key in state_data.keys():
      state_key = key

    if state_name.lower() == state_key.lower():
      return state_data[state_key]
    
  return -1

def answer_header(question_number, question_labels):
 ''' returns the header string for each answer'''
 header = "\n"*2
 header += "="*60 + "\n"
 header += "Question " + str(question_number) + "\n"
 header += question_labels[question_number] + "\n"
 header += "="*60 + "\n"
 return header

def question_1(tax):
  ''' ANSWER FOR QUESTION 1'''

  taxable_income = []
  total_returns = []

  for row in tax[1:]:
    taxable_income.append(int(row[96]))
  for row in tax[1:]:
    total_returns.append(int(row[4]))

  q1_answer = sum(taxable_income)/sum(total_returns) * 1000

  return q1_answer
  # answers.write('${:8.0f}'.format(q1_answer))

def question_2(tax):
  ''' ANSWER FOR QUESTION 2'''

  #lists to store the N1 and A04800 for each group
  group_1_tax_val = []
  group_1_returns = []

  group_2_tax_val = []
  group_2_returns = []

  group_3_tax_val = []
  group_3_returns = []

  group_4_tax_val = []
  group_4_returns = []

  group_5_tax_val = []
  group_5_returns = []

  group_6_tax_val = []
  group_6_returns = []

  for row in tax[1:]:
    if row[3] == "1":
      group_1_tax_val.append(int(row[96]))
      group_1_returns.append(int(row[4]))   

    if row[3] == "2":
      group_2_tax_val.append(int(row[96]))
      group_2_returns.append(int(row[4])) 

    if row[3] == "3":
      group_3_tax_val.append(int(row[96]))
      group_3_returns.append(int(row[4]))   

    if row[3] == "4":
      group_4_tax_val.append(int(row[96]))
      group_4_returns.append(int(row[4])) 

    if row[3] == "5":
      group_5_tax_val.append(int(row[96]))
      group_5_returns.append(int(row[4]))   

    if row[3] == "6":
      group_6_tax_val.append(int(row[96]))
      group_6_returns.append(int(row[4])) 
  
  # a list to store all the group answers
  answers_lst = []

  g1 = (sum(group_1_tax_val) / sum(group_1_returns) * 1000)
  
  g2 = ((sum(group_2_tax_val) / sum(group_2_returns) * 1000))

  g3 = ((sum(group_3_tax_val) / sum(group_3_returns) * 1000))

  g4 = ((sum(group_4_tax_val) / sum(group_4_returns) * 1000))

  g5 = ((sum(group_5_tax_val) / sum(group_5_returns) * 1000))

  g6 = ((sum(group_6_tax_val) / sum(group_6_returns) * 1000))
 
  #adds all the answers to the list
  answers_lst.append(g1)
  answers_lst.append(g2)
  answers_lst.append(g3)
  answers_lst.append(g4)
  answers_lst.append(g5)
  answers_lst.append(g6)

  return answers_lst

def question_3(tax, state_names, population_lst):
  ''' ANSWER FOR QUESTION 3'''

  #empty dictionary for storage
  question_3_dict = {}

  for data in tax[1:]:
    if data[1] not in question_3_dict:
      question_3_dict[data[1]] = {"tax": 0, "population": 0}

      state_name = get_state_name(state_names, data[1])
      
      population_value = get_state_population(population_lst, state_name)
      
      question_3_dict[data[1]]["population"] = population_value

    question_3_dict[data[1]]["tax"] += int(data[96])

  for state_code in question_3_dict:
    question_3_dict[state_code]["average"] = question_3_dict[state_code]["tax"] / question_3_dict[state_code]["population"] * 1000

  return question_3_dict

def question_4(tax, state_input):
  ''' ANSWER FOR QUESTION 4'''
  # answers.write(answer_header(4, question_labels))

  state_A04800 = 0
  state_n1 = 0

  #functions the same as list, but adding instead of storing it on the list and summing it up
  for x in range(1, len(tax)):
    if state_input == tax[x][1]:
      state_A04800 += int (tax[x] [96])
      state_n1 += int(tax[x][4])

      state_taxable_income = (state_A04800/state_n1) * 1000

  return state_taxable_income

def question_5(tax, state_input):
  ''' ANSWER FOR QUESTION 5'''
  # answers.write(answer_header(5, question_labels))
  
  #sets all the variable to 0
  g1 = 0
  g2 = 0
  g3 = 0
  g4 = 0
  g5 = 0
  g6 = 0

  for row in tax[1:]:
    if row[1] == state_input and row[3] == "1": 
      g1 = ((int(row[96]) / int(row[4]) * 1000))
      # answers.write('Group 1: ${:8.0f}\n'.format(g1))

    if row[1] == state_input and row[3] == "2":
      g2 = ((int(row[96]) / int(row[4]) * 1000))
      # answers.write('Group 2: ${:8.0f}\n'.format(g2))

    if row[1] == state_input and row[3] == "3": 
      g3 = ((int(row[96]) / int(row[4]) * 1000))
      # answers.write('Group 3: ${:8.0f}\n'.format(g3))

    if row[1] == state_input and row[3] == "4": 
      g4 = ((int(row[96]) / int(row[4]) * 1000))
      # answers.write('Group 4: ${:8.0f}\n'.format(g4))
      
    if row[1] == state_input and row[3] == "5": 
      g5 = ((int(row[96]) / int(row[4]) * 1000))
      # answers.write('Group 5: ${:8.0f}\n'.format(g5))

    if row[1] == state_input and row[3] == "6": 
      g6 = ((int(row[96]) / int(row[4]) * 1000))
      # answers.write('Group 6: ${:8.0f}\n'.format(g6))
  # a list to store all the group answers
  answers_lst = []
  #adds all the answers to the list
  answers_lst.append(g1)
  answers_lst.append(g2)
  answers_lst.append(g3)
  answers_lst.append(g4)
  answers_lst.append(g5)
  answers_lst.append(g6)

  return answers_lst

def question_6(tax, state_input):
  ''' ANSWER FOR QUESTION 6'''
  # answers.write(answer_header(6, question_labels))

  #sets all the variable to 0
  g1 = 0
  g2 = 0
  g3 = 0
  g4 = 0
  g5 = 0
  g6 = 0

  #gets all the answer for each group
  for row in tax[1:]:
    if row[1] == state_input and row[3] == "1": 
      g1 = int(row[13]) / int(row[4])
      # answers.write('Group 1: ${:8.2f}\n'.format(g1))

    if row[1] == state_input and row[3] == "2": 
      g2 = int(row[13]) / int(row[4])
      # answers.write('Group 2: ${:8.2f}\n'.format(g2))

    if row[1] == state_input and row[3] == "3": 
      g3 = int(row[13]) / int(row[4])
      # answers.write('Group 3: ${:8.2f}\n'.format(g3))

    if row[1] == state_input and row[3] == "4": 
      g4 = int(row[13]) / int(row[4])
      # answers.write('Group 4: ${:8.2f}\n'.format(g4))
      
    if row[1] == state_input and row[3] == "5": 
      g5 = int(row[13]) / int(row[4])
      # answers.write('Group 5: ${:8.2f}\n'.format(g5))

    if row[1] == state_input and row[3] == "6": 
      g6 = int(row[13]) / int(row[4])
      # answers.write('Group 6: ${:8.2f}\n'.format(g6))

  # a list to store all the group answers
  answers_lst = []
  #adds all the answers to the list
  answers_lst.append(g1)
  answers_lst.append(g2)
  answers_lst.append(g3)
  answers_lst.append(g4)
  answers_lst.append(g5)
  answers_lst.append(g6)

  return answers_lst

def question_7(tax, state_input):
  ''' ANSWER FOR QUESTION 7'''
  # answers.write(answer_header(7, question_labels))
  
  #sets all the variable to 0
  g1 = 0
  g2 = 0
  g3 = 0
  g4 = 0
  g5 = 0
  g6 = 0

  #gets all the answer for each group
  for row in tax[1:]:
    if row[1] == state_input and row[3] == "1": 
      g1 = ((int(row[4]) - int(row[95])) / int(row[4]) * 100)

    if row[1] == state_input and row[3] == "2": 
      g2 = ((int(row[4]) - int(row[95])) / int(row[4]) * 100)

    if row[1] == state_input and row[3] == "3": 
      g3 = ((int(row[4]) - int(row[95])) / int(row[4]) * 100)

    if row[1] == state_input and row[3] == "4": 
      g4 = ((int(row[4]) - int(row[95])) / int(row[4]) * 100)

    if row[1] == state_input and row[3] == "5": 
      g5 = ((int(row[4]) - int(row[95])) / int(row[4]) * 100)

    if row[1] == state_input and row[3] == "6": 
      g6 = ((int(row[4]) - int(row[95])) / int(row[4]) * 100)

  # a list to store all the group answers
  answers_lst = []
  #adds all the answers to the list
  answers_lst.append(g1)
  answers_lst.append(g2)
  answers_lst.append(g3)
  answers_lst.append(g4)
  answers_lst.append(g5)
  answers_lst.append(g6)

  return answers_lst

def question_8(tax, state_input, states_title, population_lst):
  ''' ANSWER FOR QUESTION 8'''
  #makes an empty list
  n1 = []
  #appenidng A04800 to the list
  for row in tax[1:]:
    if row[1] == state_input: 
      n1.append(int(row[96]))
      
  state_name = get_state_name(states_title, state_input)
  total_population = get_state_population(population_lst, state_name)
  return sum(n1) / total_population * 1000

def question_9(tax, state_input):
  ''' ANSWER FOR QUESTION 9'''

  #sets all the variable to 0
  g1 = 0
  g2 = 0
  g3 = 0
  g4 = 0
  g5 = 0
  g6 = 0

  #gets all the answer for each group
  state_total = []
  for row in tax[1:]:
    if row[1] == state_input:
      state_total.append(int(row[4]))
      total = sum(state_total)
    if row[1] == state_input and row[3] == "1": 
      group = int(row[4])
  g1 = (group / total) * 100

  state_total = []
  for row in tax[1:]:
    if row[1] == state_input:
      state_total.append(int(row[4]))
      total = sum(state_total)
    if row[1] == state_input and row[3] == "2": 
      group = int(row[4])
      # print(group)
  g2 = (group / total) * 100

  state_total = []
  for row in tax[1:]:
    if row[1] == state_input:
      state_total.append(int(row[4]))
      total = sum(state_total)
    if row[1] == state_input and row[3] == "3": 
      group = int(row[4])
      # print(group)
  g3 = (group / total) * 100

  state_total = []
  for row in tax[1:]:
    if row[1] == state_input:
      state_total.append(int(row[4]))
      total = sum(state_total)
    if row[1] == state_input and row[3] == "4": 
      group = int(row[4])
  g4 = (group / total) * 100

  state_total = []
  for row in tax[1:]:
    if row[1] == state_input:
      state_total.append(int(row[4]))
      total = sum(state_total)
    if row[1] == state_input and row[3] == "5": 
      group = int(row[4])
      # print(group)
  g5 = (group / total) * 100

  state_total = []
  for row in tax[1:]:
    if row[1] == state_input:
      state_total.append(int(row[4]))
      total = sum(state_total)
    if row[1] == state_input and row[3] == "6": 
      group = int(row[4])
      # print(group)
  g6 = (group / total) * 100

  # a list to store all the group answers
  answers_lst = []
  #adds all the answers to the list
  answers_lst.append(g1)
  answers_lst.append(g2)
  answers_lst.append(g3)
  answers_lst.append(g4)
  answers_lst.append(g5)
  answers_lst.append(g6)

  return answers_lst

def question_10(tax, state_input):
  ''' ANSWER FOR QUESTION 10'''

  #sets all the variable to 0
  g1 = 0
  g2 = 0
  g3 = 0
  g4 = 0
  g5 = 0
  g6 = 0
  
  #gets all the answer for each group
  state_total = []
  for row in tax[1:]:
    if row[1] == state_input:
      state_total.append(int(row[96]))
      total = sum(state_total)
    if row[1] == state_input and row[3] == "1": 
      group = int(row[96])
  g1 = (group / total) * 100

  state_total = []
  for row in tax[1:]:
    if row[1] == state_input:
      state_total.append(int(row[96]))
      total = sum(state_total)
    if row[1] == state_input and row[3] == "2": 
      group = int(row[96])
  g2 = (group / total) * 100

  state_total = []
  for row in tax[1:]:
    if row[1] == state_input:
      state_total.append(int(row[96]))
      total = sum(state_total)
    if row[1] == state_input and row[3] == "3": 
      group = int(row[96])
  g3 = (group / total) * 100

  state_total = []
  for row in tax[1:]:
    if row[1] == state_input:
      state_total.append(int(row[96]))
      total = sum(state_total)
    if row[1] == state_input and row[3] == "4": 
      group = int(row[96])
  g4 = (group / total) * 100

  state_total = []
  for row in tax[1:]:
    if row[1] == state_input:
      state_total.append(int(row[96]))
      total = sum(state_total)
    if row[1] == state_input and row[3] == "5": 
      group = int(row[96])
  g5 = (group / total) * 100
  
  state_total = []
  for row in tax[1:]:
    if row[1] == state_input:
      state_total.append(int(row[96]))
      total = sum(state_total)
    if row[1] == state_input and row[3] == "6": 
      group = int(row[96])
  g6 = (group / total) * 100

  # a list to store all the group answers
  answers_lst = []
  #adds all the answers to the list
  answers_lst.append(g1)
  answers_lst.append(g2)
  answers_lst.append(g3)
  answers_lst.append(g4)
  answers_lst.append(g5)
  answers_lst.append(g6)

  return answers_lst

def main():
  ''' MAIN FUNCTION'''
  #get the url using json
  population_lst = get_data_from_internet('https://raw.githubusercontent.com/heymrhayes/class_files/main/state_populations_2018.txt', 'json')

  #get the csv file
  tax = get_data_from_file('tax_return_data_2018.csv')

  #get the json file
  states_title = get_data_from_file('states_titlecase.json')

  #an input for the state to enter
  state_input = input(str('Enter a State: '))

  #the questions for the header
  question_labels = [
   "",
   "average taxable income per return across all groups",
   "average taxable income per return for each agi group",
   "average taxable income (per resident) per state",
   "average taxable income per return across all groups",
   "average taxable income per return for each agi group",
   "average dependents per return for each agi group",
   "percentage of returns with no taxable income per agi group",
   "average taxable income per resident",
   "percentage of returns for each agi_group",
   "percentage of taxable income for each agi_group"
 ]

  #variables to store the answers for the questions
  ans_q1 = question_1(tax)
  ans_q2 = question_2(tax)
  ans_q3 = question_3(tax, states_title, population_lst)
  ans_q4 = question_4(tax, state_input)
  ans_q5 = question_5(tax, state_input)
  ans_q6 = question_6(tax, state_input)
  ans_q7 = question_7(tax, state_input)
  ans_q8 = question_8(tax, state_input, states_title, population_lst)
  ans_q9 = question_9(tax, state_input)
  ans_q10 = question_10(tax, state_input)

  ############################################
  '''ANSWER.TXT WRITING'''
  ############################################
  answers = open('answers' + state_input + '.txt', 'w')
  
  # Writing question 1
  answers.write(answer_header(1, question_labels))
  answers.write("${:8.0f}".format(ans_q1))

  # Writing question 2
  answers.write(answer_header(2, question_labels))
  index_q2 = 1

  for group_data in ans_q2:
    answers.write("Group " + str(index_q2) + ": ${:8.0f}".format( group_data ) + "\n")
    index_q2 += 1

  # Writing question 3
  answers.write(answer_header(3, question_labels))
  for state_code in ans_q3:
    answers.write(state_code + ": ${:8.0f}".format(ans_q3[state_code]["average"]) + '\n')

  # Writing question 4
  answers.write(answer_header(4, question_labels))
  answers.write("${:8.0f}".format(ans_q4))

  # Writing question 5
  answers.write(answer_header(5, question_labels))
  index_q5 = 1

  for group_data in ans_q5:
    answers.write("Group " + str(index_q5) + ": ${:8.0f}".format( group_data ) + "\n")
    index_q5 += 1

  # Writing question 6
  answers.write(answer_header(6, question_labels))
  index_q6 = 1

  for group_data in ans_q6:
    answers.write("Group " + str(index_q6) + ": {:8.2f}".format( group_data ) + "\n")
    index_q6 += 1

  # Writing question 7
  answers.write(answer_header(7, question_labels))
  index_q7 = 1

  for group_data in ans_q7:
    answers.write("Group " + str(index_q7) + ": {:8.2f}%".format( group_data ) + "\n")
    index_q7 += 1

  # Writing question 8
  answers.write(answer_header(8, question_labels))
  answers.write("${:8.0f}".format(ans_q8))

  # Writing question 9
  answers.write(answer_header(9, question_labels))
  index_q9 = 1

  for group_data in ans_q9:
    answers.write("Group " + str(index_q9) + ": {:8.2f}%".format( group_data ) + "\n")
    index_q9 += 1

  # Writing question 10
  answers.write(answer_header(10, question_labels))
  index_q10 = 1

  for group_data in ans_q10:
    answers.write("Group " + str(index_q10) + ": {:8.2f}%".format( group_data ) + "\n")
    index_q10 += 1


  #######################################
  ''' VISUALIZATION '''
  #######################################
  group_labels = ["group 1", "group 2", "group 3", "group 4", "group 5", "group 6"]

  # Pie-chart 1 for question 9
  plt.clf()
  plt.pie(ans_q9, labels = group_labels, autopct = "%1.2f%%", shadow = True)
  plt.title("Average returns for each agi per state")
  plt.savefig("pie1_" + state_input + ".png")

  # Pie-chart 2 for question 10
  plt.clf()
  plt.pie(ans_q10, labels = group_labels, autopct = "%1.2f%%", shadow = True)
  plt.title("Average taxable for each agi per state")
  plt.savefig("pie2_" + state_input + ".png")

  # Vertical bar chart
  plt.clf()
  state_code_lst = []
  state_avgs_lst = []

  new_dict_q3 = {}

  for key in ans_q3:
    new_dict_q3[key] = ans_q3[key]["average"]

  sorted_dict_q3 = dict(sorted(new_dict_q3.items(), key=operator.itemgetter(1), reverse=True))

  # print(sorted_dict_q3)

  for state_code_key in sorted_dict_q3:
    state_code_lst.append(state_code_key)
    state_avgs_lst.append(sorted_dict_q3[state_code_key])

  plt.bar(state_code_lst, state_avgs_lst)
  plt.title("Average Taxable Income for National Level")
  plt.savefig("bar_" + state_input + ".png")

  # plt.show()

main()