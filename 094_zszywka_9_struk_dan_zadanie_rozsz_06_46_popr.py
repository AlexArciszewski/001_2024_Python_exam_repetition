# Zad 6.
# Wyboraź sobie, że otrzymałeś z API następujące dane:

{
    data: [1, 2, 'asd', [2, 3, 4, 5]],
    'nested_analysis': {
        'analysis_1': [1, 10, 15, 120.2, '120'],
        'analysis_2': [10, 100, 'test', 200, 300],
    },
    'probes': [['probe_1', 'probe_2'], 'probe_3']
}

# Twoim zadaniem jest wyłuskanie spod każdego klucza w powyższym słowniku tylko tych danych,
# które są typu str i wyświetlić je na ekranie.

# data_dict = {
#     data: [1, 2, 'asd', [2, 3, 4, 5]],
#     'nested_analysis': {
#         'analysis_1': [1, 10, 15, 120.2, '120'],
#         'analysis_2': [10, 100, 'test', 200, 300],
#     },
#     'probes': [['probe_1', 'probe_2'], 'probe_3']
# }
#
# for asset in data_dict:
#     print(asset)