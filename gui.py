from operator import index
import streamlit as st
from numscan import get_details
import folium
from streamlit_folium import folium_static 
import pandas as pd

st.title("Phone Reconnaissance")
phno = st.text_input("Phone number :", placeholder="ex: 911234567890")
st.markdown("""---""")

if(phno):
    try: 
        details = get_details(phno)
        del details['number']
        del details['country_prefix']        
        #st.success("Success")
        st.subheader("General Details :")
        
        Data = pd.DataFrame({0:[k.capitalize() for k in details.keys()], 1:[str(v) for v in details.values()]})
        st.dataframe(Data)

        geomap = folium.Map(location=details['coordinates'], zoom_start=6)
        folium.Marker(details['coordinates'], popup=details["location"]).add_to((geomap))

        #coords = map(float, details['Coordinates'].split(","))
        
        geodata = dict()
        geodata ['Country'] = details["country_name"]
        geodata ['Location'] = details["location"]
        geodata ['Coordinates'] = str(details["coordinates"])
        df = pd.DataFrame(geodata,  index=[0])

        st.markdown("""---""")

        st.subheader("Geolocation :")
        st.dataframe(df)
        folium_static(geomap)

        st.warning("NOTE : THIS APP CAN ONLY BE USED 100 TIMES A MONTH !")

    except Exception as error:
        st.error(error)


