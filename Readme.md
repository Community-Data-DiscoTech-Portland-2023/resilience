
## Resilience Project Group

2024 City of Portland 2023 Open Data Disco Tech - Resiliency data

Open notes document
Room - Resiliency data
March 2, 2024 


For coding contribs: https://github.com/orgs/Community-Data-DiscoTech-Portland-2023/repositories 


Data sources:
Open Data - https://www.portland.gov/bps/smart-city-pdx 
Portland Maps Open Data https://gis-pdx.opendata.arcgis.com/
Multnomah County Open Data: https://gis-multco.opendata.arcgis.com/
Open data metadata library - https://www.portlandmaps.com/metadata/

Oregon Metro Open Data: https://gis.oregonmetro.gov/
DOGAMI: https://www.oregon.gov/dogami/gis/Pages/index.aspx


Emergency maps: https://gis-pdx.opendata.arcgis.com/search?q=emergency 
Tree canopy inventories: https://gis-pdx.opendata.arcgis.com/search?q=tree%20 
Heatmap data from PSU- 
Heatmap from mult co - HVI_2023 (arcgis.com) 
Instructions: Add your notes here. Follow the Code of Conduct for the event. Enjoy.

Project: Equitable Cooling Access: 
Where can people go to cool down when it’s hot in Portland?  Is there equitable cooling opportunity access and where can cooling centers be added to mitigate areas where cooling is lacking? Are there transportation options available for people in high-impact areas to access cooling? 

Stage 1: which areas are most lacking in terms of needed cooling centers in the three various heat scenarios? 
Stage 2: where might new cooling centers be located (zoning data, etc?) to meet needs? 

Heat Index: 3 Heat level scenarios? 
Scenario 1: access to public outdoors pools, rivers, lakes 
Scenario 2: access to public outdoors pools, but not rivers and lakes (algae blooms) 
Scenario 3: Too hot for public outdoors pools or rivers and lakes  

Counties:  Multnomah, Clackamas, Washington, Yamhill

Public pools - at which temp levels do they close?  [initial search suggests there may not be a set temperature–no policy, just vibes? During heat advisories - also depends on relative humidity]
Cooling centers location, access,
River access / algae blooms
Heat deaths
Sovi data:    Population of Elderly/disabled/youth/seniors living alone/male/health issues/density/tree canopy/impervious surfaces/mean surface temps (metro land access data).  

Toxic Algae notes: not tied to specific air temperature levels; measured by sighting reports and chemical measurements.  
Water
Freshwater access in event of emergency
Sewage
River data
Flooding in event of earthquake
Algae Blooms, fish survival, water quality (heat data very relevant here) adjacency to socially vulnerable areas

Possible data sources: 
Flooding Map for Portland: https://gis-pdx.opendata.arcgis.com/datasets/c24e074759624846977a68fa12418473_116/explore?location=45.494778%2C-122.686512%2C9.79
Cascadia maps
Dogami: https://gis.dogami.oregon.gov/arcgis/rest/services/HV/StatewideEQ/MapServer
NOAA
FEMA
Vulnerability index / equity
https://www.fema.gov/flood-maps/national-flood-hazard-layer
Heat map data from PSU
Emergency maps: https://gis-pdx.opendata.arcgis.com/search?q=emergency 
Oregon State: Precipitation
Portland Sewer Pipes: https://pdx.maps.arcgis.com/apps/Viewer/index.html?appid=60bbdb13e97849f898713304dd20b9ad#!
Drinking fountain maps: https://gis-pdx.opendata.arcgis.com/datasets/52a5e1b42486426cb1900d93347cf68e_84/explore
River Bathymetry: https://gis-pdx.opendata.arcgis.com/datasets/e9171db2be9b48d6b9462813fcd477b7_194/explore
River Depth: https://gis-pdx.opendata.arcgis.com/datasets/714855156eda48f498edeed01d517d7f_205/explore
Watersheds: https://gis-pdx.opendata.arcgis.com/datasets/714855156eda48f498edeed01d517d7f_205/explore
Wetlands: 
https://gis-pdx.opendata.arcgis.com/maps/47ec45260dc34ce7ae4ab9a804080ca3
River Overlay Boundary: https://gis-pdx.opendata.arcgis.com/maps/f3e8fd88cf884d01bfa74c2ccfe42131

USGS Oregon River Data: https://waterdata.usgs.gov/or/nwis/rt


From Hugh: Centerline data for rivers (openstreetmap) with overlay for census data buffer 100 meters around centerline to pull in census tracts (sovi census data index, tigerstripe census block group data) 

https://www.portland.gov/water/equity   Need Microsoft Acct  can login with github

Heat Deaths from heat multnomah county - Reports and Analysis of Heat Events | Multnomah County (multco.us)

Stream Centerlines:
https://gis-pdx.opendata.arcgis.com/datasets/c3d43b153dd441efb4b0d2ab66d2ae8d_128/explore

Predictive Heat Index/Tree Canopy 
Data sources: 
tree canopy - https://experience.arcgis.com/experience/7556b8b1017949cdb56145ec33aef814/page/mobile/

Heat maps
Predictive summer temps


Cooling centers: https://www.portland.gov/bps/cleanenergy/news/2023/11/6/portland-bureau-planning-and-sustainabilitys-cooling-portland


Parks tree inventory : 
https://gis-pdx.opendata.arcgis.com/datasets/15ae00ece1bf486a868c0f635d3acbfa_220/explore?location=45.550554%2C-122.632400%2C11.56

https://experience.arcgis.com/experience/0af8ec76c2024e6980bf83771a165a0a/page/Adaptive-Capacity/?data_id=dataSource_34-hvi_ranked_20230306_2_8494%3A180%2CdataSource_6-HVI_20221209_3996%3A180%2CdataSource_7-HVI_20221209_3996%3A180%2CdataSource_8-HVI_20221209_3996%3A180%2CdataSource_9-HVI_20221209_3996%3A180%2CdataSource_10-HVI_20221209_3996%3A180%2CdataSource_11-HVI_20221209_3996%3A180%2CdataSource_12-HVI_20221209_3996%3A180%2CdataSource_19-HVI_20221209_3996%3A180%2CdataSource_20-HVI_20221209_3996%3A180%2CdataSource_21-HVI_20221209_3996%3A180%2CdataSource_22-HVI_20221209_3996%3A180%2CdataSource_23-HVI_20221209_3996%3A180%2CdataSource_13-HVI_20221209_3996%3A180%2CdataSource_14-HVI_20221209_3996%3A180%2CdataSource_15-HVI_20221209_3996%3A180%2CdataSource_16-HVI_20221209_3996%3A180%2CdataSource_17-HVI_20221209_3996%3A180%2CdataSource_29-HVI_20230124_ac_5053%3A180%2CdataSource_35-hvi_ranked_sens_edit_3694%3A180%2CdataSource_27-hvi_ranked_sens_edit_6823%3A180%2CdataSource_31-hvi_ranked_20230306_2_8494%3A180%2CdataSource_33-hvi_ranked_20230306_2_8494%3A180


Heat vulnerability index: https://experience.arcgis.com/experience/0af8ec76c2024e6980bf83771a165a0a/page/Sensitivity/ 

Map of Cooling Centers/Pools - multnomah county 2023
https://www.arcgis.com/apps/webappviewer/index.html?id=0856c38202954fc19ce55f4d60794324&extent=-13680705.1509%2C5685177.4191%2C-13610383.0849%2C5725536.17%2C102100
Washington County: https://experience.arcgis.com/experience/80d588f139b640dab4e3690593205749/


Climate layers in RLIS
Metro Urban Heat Islands


Reference, from Heat Vulnerability Index methodology: 
P. 5 == indicators included  the HVI
https://multco-web7-psh-files-usw2.s3-us-west-2.amazonaws.com/s3fs-public/HeatVulnerabilityIndex_Methods_Report.pdf 



Disruptive thinking

Adult binge drinking by county, Oregon : 
https://www.oregon.gov/oha/PH/ABOUT/Documents/indicators/bingedrinking-county.pdf

Questions



----------------------------------------------

### Datasources
