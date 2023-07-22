import joblib
import 

def app_recommend(Apps_df, similarity, appID):
  """load save model"""
 # Apps_df = joblib.load('apps_dict.pkl')
 # similarity = joblib.load('similarity.pkl')

  apps_index = Apps_df[Apps_df['asin'] == appID].index[0]
  distances = similarity[apps_index]
  apps_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

 for i in apps_list:
 print(apps_df.iloc[i[0]].asin)


class Apps_Reccomendation_Model():
  def __init__(self):
    self.model = joblib.load('Recommend_model.pkl')
    self.Apps_df = joblib.load('apps_dict.pkl')
    self.similarity = joblib.load('similarity.pkl')

  def integral_recommend(self, userID: None, appID:None):
    if userID is not None and appID is None:
      print('Reccommended apps based on your previous download')
      reccomend = Apps_recommendations(self.model, userID, k=5)
      print(reccomend)

    elif userID is None and appID is not None:
      print('Reccommended items based on current view/likes:')
      app_recommend(self.Apps_df, self.similarity, appID)

    elif userID is not None and appID is not None:
      print('Reccommended items based on current view/likes:')
      app_recommend(self.Apps_df, self.similarity, appID)

      print('Reccommended apps based on your previous download')
      reccomend = Apps_recommendations(self.model, userID, k=5)
      print(reccomend)
    else:
      print('provide your ID or view one of the apps')