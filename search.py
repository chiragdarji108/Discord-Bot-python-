_author__ = 'jcgregorio@google.com (Joe Gregorio)'

import pprint

from googleapiclient.discovery import build


def search_main(query):
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  # Handle if no search results found
  service = build("customsearch", "v1",
            developerKey="GOOGLE_DEVELOPER_KEY")

  res = service.cse().list(
      q=query,
      cx='SEARCH_ENGINE_ID_HERE',
    ).execute()
  print("response", res)
  try:
    items = res["items"]
    top_five_links = []
    for i in items:
        if(len(top_five_links)<5):
            top_five_links.append(i["link"])
    pprint.pprint(res["items"])
    print(top_five_links)
    return top_five_links
  except:
    return
