import csv, urllib

def load_csv(url):
   d = {}
   fish_data=[]
   date_data=[]
   fp = urllib.urlopen(url)
   for row in csv.reader(fp):
      fish_data.append(row[1])
      date_data.append(row[0])
   fish_data.remove('fish')
   date_data.remove('date')
   return fish_data, date_data

def make_dates_dict(fish_data, date_data):

   fish_dict = {}
   
   unique_fish=set(fish_data)
   print unique_fish
   unique_fish_list=list(unique_fish)

   
   
   for h in unique_fish_list:
      date_list=[]
      for i in range(0,len(fish_data)-1):
         if fish_data[i]==h:

            date_list.append(date_data[i])
      temp=set(date_list)
      date_list=list(temp)
      date_list.sort()
      fish_dict[h]=date_list

   return fish_dict
   


def make_fish_dict(fish_data, date_data):
   
   fish_name_list=[]
   date_dict={}
   for i in range(0,len(fish_data)-1):

      if i==0:
         current=date_data[i]
         fish_name_list=[]
         fish_name_list.append(fish_data[i])
         date_dict[current]=fish_name_list
      elif date_data[i]==current:
         #do something
         fish_name_list.append(fish_data[i])
         date_dict[current]=fish_name_list
      else:
         #do something. date_data[i] is not equal to current.
         date_dict[current]=fish_name_list
         current=date_data[i]
         fish_name_list=[]
         fish_name_list.append(fish_data[i])

   return date_dict
   
   
   
def get_fishes_by_date(fish_d, date):
   fishlist = []
   fishlist=fish_d[date]
   return fishlist
   
   
def get_dates_by_fish(dates_d, fish):
   dateslist = []
   dateslist=dates_d[fish]

   return dateslist
   
fish_data, date_data = load_csv('https://raw.github.com/ctb/edda/master/doc/beacon-2011/tutorial5/fishies.csv')

#dates_d is a dictionary with a list of the unique fish, and each fish has a list of dates.
dates_d = make_dates_dict(fish_data, date_data)

fish_d = make_fish_dict(fish_data, date_data)

date='1/1'
fish='plaice'

print 'Fish that were eaten on ' + date + ':\n'
print get_fishes_by_date(fish_d, date)
print '\nDates that ' + fish + ' was eaten on:\n'
print get_dates_by_fish(dates_d, fish)

# test 1
x = get_fishes_by_date(fish_d, '1/1')
assert 'salmon' in x

###

# test 2
x = get_dates_by_fish(dates_d, 'salmon')
assert '1/1' in x
assert '1/2' in x

###

# test 3
x = get_fishes_by_date(fish_d, '1/1')
assert 'salmon' in x, x

###

# test 4
x = get_dates_by_fish(dates_d, 'salmon')
assert '1/1' in x

