
import pandas as pd

df0 = pd.read_csv('dataset/ccrb-raw-2021.csv',
				dtype={
					'IncidentRank': 'string',
					'IncidentRankLong': 'string',
					'IncidentCommand': 'string',
					'IncidentDate': 'string',
					'PenaltyRec': 'string',
					'NYPDDisposition': 'string',
					'PenaltyDesc': 'string',
					'LocationType': 'string',
					'ContactReason': 'string',
					'ContactOutcome': 'string',
					'IncidentPrecinct': 'string',
					'ImpactedRace': 'string',
					'ImpactedGender': 'string'
					})
df0 = df0.fillna('')

df1 = df0.iloc[:, [19, 21, 31, 32]]
print(df1.info())

# print(df.info())

labels = ['Closed - Pending Litigation', 'Exonerated', 'Miscellaneous', 
		 'Substantiated', 'Truncated', 'Unfounded', 'Unsubstantiated']

# df = df.drop(['AllegationID', 'OfficerID', 'CurrentRank', 'CurrentRankLong', 'Status', 'IncidentCommand', 'ComplaintID', 'ShieldNo', 'IncidentRank', 'IncidentRankLong', 'IncidentDate', 'LocationType', 'CloseDate', 'ReceivedDate'], axis=1)
# print(df[:5])
# df = df['IncidentDate'].fillna('')
# print(df['IncidentDate'])
# print(df0.info())
# print(df['ContactOutcome'])
# df.head()
# print(df.shape[0])
# print(df.describe)
# print(df.isnull().any())
# print(df.isnull().sum())
# is_error = pd.to_numeric(df['CurrentCommand'], errors='coerce').isna()
# df[is_error]
