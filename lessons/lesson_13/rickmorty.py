import requests
import time

class RickMortyExtractor:

    def __init__(self):
        self.base_url = "https://rickandmortyapi.com/api"


    def _get_data(self, endpoint, params=None):

        data = []
        url = f"{self.base_url}/{endpoint}"

        while url:
            print(url)
            time.sleep(3)
            try:
                response = requests.get(url, params=params, timeout=30)
                print(params)
                response.raise_for_status()
                curr_page_response = response.json()
                data.extend(curr_page_response["results"])
                url = curr_page_response["info"]["next"]
                params = None
            
            except requests.exceptions.RequestException as e:
                print(f"Reuqest failed: {e}")
                break
            except KeyError as e:
                print(f"Missing expected field in response: {e}")
                break
            except ValueError as e:
                print("Invalid JSON response")
                break
            except Exception as e:
                print(f"Unexpected error: {e}")
                break

        return data

    def get_characters(self, name=None, status=None, species=None, gender=None, type=None):

        params = {"name": name,
                  "status": status,
                  "species": species,
                  "gender": gender,
                  "type": type}
        
        return self._get_data("character", params)

    def get_episodes(self, name=None, episode=None):
        params = {"name": name,
                  "episode": episode}
        
        return self._get_data("episode", params)
    

    def get_locations(self, name=None, loc_type=None, dimension=None):
        params = {
            "name": name,
            "type": loc_type,
            "dimension": dimension
        }

        return self._get_data("location", params)
     
    
rickmorty = RickMortyExtractor()
character_data = rickmorty.get_characters()