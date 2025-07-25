clean_dates = ['2025-07-25', '2025-07-26', '2025-08-08', '2025-08-11', '2025-08-13']
meeting_list = ['PyCon Russia 2025', 'PyOhio 2025', 'Buea - Creating Python Communities and outreach', 'DjangoCon Africa 2025', 'PyCon Somalia 2025']
events = []

for t,m in zip(clean_dates, meeting_list):
    event = {'time': t, 'name':m}
    events.append(event)
print(events)
events_dict = {}


for i, event in enumerate(events, start=1):
    events_dict[i] = event

print(events_dict)
# {
#     1: {'time': '2025-07-25', 'name': 'PyCon Russia 2025'},
#     2: {'time': '2025-07-26', 'name': 'PyOhio 2025'},
#     3: {'time': '2025-08-08', 'name': 'Buea - Creating Python Communities and outreach'},
#     4: {'time': '2025-08-11', 'name': 'DjangoCon Africa 2025'},
#     5: {'time': '2025-08-13', 'name': 'PyCon Somalia 2025'}
# }
