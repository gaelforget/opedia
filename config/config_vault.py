#!/usr/bin/env python

import os

def makedir(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)
	return

def leafStruc(base):
	nrt = base + 'nrt/'
	makedir(nrt)
	rep = base + 'rep/'
	makedir(rep)
	doc = base + 'doc/'
	makedir(doc)
	code = base + 'code/'
	makedir(code)
	return nrt, rep, doc, code


opedia_proj = r'H:/Dropbox/projects/opedia/'
vault = r'H:/Dropbox/Apps/OpediaVault/'


# opedia_proj = r'/home/nrhagen/Documents/opedia'
# vault = r'/run/user/1000/gvfs/afp-volume\:host\=cmap_vault.local\,user\=nrhagen\,volume\=vault/'

makedir(vault)


################## opedia vault file structure ##################
vault_raw = vault #+ 'raw/'
makedir(vault_raw)

#########  assimilation  #########
assimilation_raw = vault_raw + 'assimilation/'
makedir(assimilation_raw)


###########  models  ##########
model_raw = vault_raw + 'model/'
makedir(model_raw)
### models/mercator_pisces ####
mercator_pisces_raw = model_raw + 'mercator_pisces/'
makedir(mercator_pisces_raw)
nrt_mercator_pisces_raw, rep_mercator_pisces_raw, doc_mercator_pisces_raw, code_mercator_pisces_raw = leafStruc(mercator_pisces_raw)
nrt_mercator_pisces_prefix = 'mercator_pisces_'
rep_mercator_pisces_prefix = 'mercator_pisces_'
### models/mercator_mld ####
mercator_mld_raw = model_raw + 'mercator_mld/'
makedir(mercator_mld_raw)
nrt_mercator_mld_raw, rep_mercator_mld_raw, doc_mercator_mld_raw, code_mercator_mld_raw = leafStruc(mercator_mld_raw)
nrt_mercator_mld_prefix = 'mercator_mld_'
rep_mercator_mld_prefix = 'mercator_mld_'
######## models/darwin ########
darwin_raw = model_raw + 'darwin/'
makedir(darwin_raw)
nrt_darwin_raw, rep_darwin_raw, doc_darwin_raw, code_darwin_raw = leafStruc(darwin_raw)
nrt_darwin_prefix = 'darwin_'
rep_darwin_prefix = 'darwin_'
######## models/darwin_climatology ########
darwin_clim_1992_2011_raw = model_raw + 'darwin_climatology_1992_2011/'
makedir(darwin_clim_1992_2011_raw)
nrt_darwin_clim_raw, rep_darwin_clim_raw, doc_darwin_clim_raw, code_darwin_clim_raw = leafStruc(darwin_clim_1992_2011_raw)
nrt_darwin_clim_prefix = 'darwin_clim_'
rep_darwin_clim_prefix = 'darwin_clim_'

######## models/darwin_Nutrient ########
darwin_Nutrient_raw = model_raw + 'darwin_Nutrient/'
makedir(darwin_Nutrient_raw)
nrt_darwin_Nutrient_raw, rep_darwin_Nutrient_raw, doc_darwin_Nutrient_raw, code_darwin_Nutrient_raw = leafStruc(darwin_Nutrient_raw)
nrt_darwin_Nutrient_prefix = 'darwin_Nutrient_'
rep_darwin_Nutrient_prefix = 'darwin_Nutrient_'

######## models/darwin_Ocean_Color ########
darwin_Ocean_Color_raw = model_raw + 'darwin_Ocean_Color/'
makedir(darwin_Ocean_Color_raw)
nrt_darwin_Ocean_Color_raw, rep_darwin_Ocean_Color_raw, doc_darwin_Ocean_Color_raw, code_darwin_Ocean_Color_raw = leafStruc(darwin_Ocean_Color_raw)
nrt_darwin_Ocean_Color_prefix = 'darwin_Ocean_Color_'
rep_darwin_Ocean_Color_prefix = 'darwin_Ocean_Color_'


######## models/darwin_Ecosystem ########
darwin_Ecosystem_raw = model_raw + 'darwin_Ecosystem/'
makedir(darwin_Ecosystem_raw)
nrt_darwin_Ecosystem_raw, rep_darwin_Ecosystem_raw, doc_darwin_Ecosystem_raw, code_darwin_Ecosystem_raw = leafStruc(darwin_Ecosystem_raw)
nrt_darwin_Ecosystem_prefix = 'darwin_Ecosystem_'
rep_darwin_Ecosystem_prefix = 'darwin_Ecosystem_'

######## models/darwin_Phytoplankton ########
darwin_Phytoplankton_raw = model_raw + 'darwin_Phytoplankton/'
makedir(darwin_Phytoplankton_raw)
nrt_darwin_Phytoplankton_raw, rep_darwin_Phytoplankton_raw, doc_darwin_Phytoplankton_raw, code_darwin_Phytoplankton_raw = leafStruc(darwin_Phytoplankton_raw)
nrt_darwin_Phytoplankton_prefix = 'darwin_Phytoplankton_'
rep_darwin_Phytoplankton_prefix = 'darwin_Phytoplankton_'






#########  observations  #########
obs_raw = vault_raw + 'observation/'
makedir(obs_raw)
in_situ_raw = obs_raw + 'in-situ/'
makedir(in_situ_raw)
remote_raw = obs_raw + 'remote/'
makedir(remote_raw)
#########  obs/in-situ/cruise  #########
cruise_raw = in_situ_raw + 'cruise/'
makedir(cruise_raw)
######  obs/in-situ/cruise/WOA_climatology  ######
WOA_climatology_raw = cruise_raw + 'WOA_climatology/'
makedir(WOA_climatology_raw)
nrt_WOA_climatology_raw, rep_WOA_climatology_raw, doc_WOA_climatology_raw, code_WOA_climatology_raw = leafStruc(WOA_climatology_raw)
######  obs/in-situ/cruise/socat  ######
socat_raw = cruise_raw + 'socat/'
makedir(socat_raw)
nrt_socat_raw, rep_socat_raw, doc_socat_raw, code_socat_raw = leafStruc(socat_raw)
####  obs/in-situ/cruise/seaflow  #####
seaflow_raw = cruise_raw + 'seaflow/'
makedir(seaflow_raw)
nrt_seaflow_raw, rep_seaflow_raw, doc_seaflow_raw, code_seaflow_raw = leafStruc(seaflow_raw)
####  obs/in-situ/cruise/flombaum   #####
flombaum_raw = cruise_raw + 'flombaum/'
makedir(flombaum_raw)
nrt_flombaum_raw, rep_flombaum_raw, doc_flombaum_raw, code_flombaum_raw = leafStruc(flombaum_raw)
####  obs/in-situ/cruise/Global_PicoPhytoPlankton   #####
Global_PicoPhytoPlankton_raw = cruise_raw + 'Global_PicoPhytoPlankton/'
makedir(Global_PicoPhytoPlankton_raw)
nrt_Global_PicoPhytoPlankton_raw, rep_Global_PicoPhytoPlankton_raw, doc_Global_PicoPhytoPlankton_raw, code_Global_PicoPhytoPlankton_raw = leafStruc(Global_PicoPhytoPlankton_raw)
####  obs/in-situ/cruise/lineage  #####
lineage_raw = cruise_raw + 'lineage/'
makedir(lineage_raw)
nrt_lineage_raw, rep_lineage_raw, doc_lineage_raw, code_lineage_raw = leafStruc(lineage_raw)
####  obs/in-situ/cruise/tax16s  #####
tax16s_raw = cruise_raw + 'tax16s/'
makedir(tax16s_raw)
nrt_tax16s_raw, rep_tax16s_raw, doc_tax16s_raw, code_tax16s_raw = leafStruc(tax16s_raw)
####  obs/in-situ/cruise/KM1314_cobalamine  #####
KM1314_cobalamin_raw = cruise_raw + 'KM1314_cobalamin/'
makedir(KM1314_cobalamin_raw)
nrt_KM1314_cobalamin_raw, rep_KM1314_cobalamin_raw, doc_KM1314_cobalamin_raw, code_KM1314_cobalamin_raw = leafStruc(KM1314_cobalamin_raw)
####  obs/in-situ/cruise/esv  #####
esv_raw = cruise_raw + 'esv/'
makedir(esv_raw)
nrt_esv_raw, rep_esv_raw, doc_esv_raw, code_esv_raw = leafStruc(esv_raw)
####  obs/in-situ/cruise/BiGRAPA1_CTDData_Chisholm  #####
BiGRAPA1_CTDData_Chisholm_raw = cruise_raw + 'BiGRAPA1_CTDData_Chisholm/'
makedir(BiGRAPA1_CTDData_Chisholm_raw)
nrt_BiGRAPA1_CTDData_Chisholm_raw, rep_BiGRAPA1_CTDData_Chisholm_raw, doc_BiGRAPA1_CTDData_Chisholm_raw, code_BiGRAPA1_CTDData_Chisholm_raw = leafStruc(BiGRAPA1_CTDData_Chisholm_raw)
####  obs/in-situ/cruise/AMT13_Chisholm  #####
AMT13_Chisholm_raw = cruise_raw + 'AMT13_Chisholm/'
makedir(AMT13_Chisholm_raw)
nrt_AMT13_Chisholm_raw, rep_AMT13_Chisholm_raw, doc_AMT13_Chisholm_raw, code_AMT13_Chisholm_raw = leafStruc(AMT13_Chisholm_raw)
####  obs/in-situ/cruise/SingleCellGenomes_Chisholm  #####
SingleCellGenomes_Chisholm_raw = cruise_raw + 'SingleCellGenomes_Chisholm/'
makedir(SingleCellGenomes_Chisholm_raw)
nrt_SingleCellGenomes_Chisholm_raw, rep_SingleCellGenomes_Chisholm_raw, doc_SingleCellGenomes_Chisholm_raw, code_SingleCellGenomes_Chisholm_raw = leafStruc(SingleCellGenomes_Chisholm_raw)
####  obs/in-situ/cruise/HOT224  #####
HOT224_raw = cruise_raw + 'HOT224/'
makedir(HOT224_raw)
nrt_HOT224_raw, rep_HOT224_raw, doc_HOT224_raw, code_HOT224_raw = leafStruc(HOT224_raw)
####  obs/in-situ/cruise/gradients_16s  #####
gradients_16s_raw = cruise_raw + 'gradients_16s/'
makedir(gradients_16s_raw)
nrt_gradients_16s_raw, rep_gradients_16s_raw, doc_gradients_16s_raw, code_gradients_16s_raw = leafStruc(gradients_16s_raw)
####  obs/in-situ/cruise/gradients_18s  #####
gradients_18s_raw = cruise_raw + 'gradients_18s/'
makedir(gradients_18s_raw)
nrt_gradients_18s_raw, rep_gradients_18s_raw, doc_gradients_18s_raw, code_gradients_18s_raw = leafStruc(gradients_18s_raw)

####  obs/in-situ/cruise/mesoscopee  #####
mesoscope_raw = cruise_raw + 'mesoscope/'
makedir(mesoscope_raw)
nrt_mesoscope_raw, rep_mesoscope_raw, doc_mesoscope_raw, code_mesoscope_raw = leafStruc(mesoscope_raw)

####  obs/in-situ/cruise/Falkor_2018  #####
Falkor_2018_raw = cruise_raw + 'Falkor_2018/'
makedir(Falkor_2018_raw)
nrt_Falkor_2018_raw, rep_Falkor_2018_raw, doc_Falkor_2018_raw, code_Falkor_2018_raw = leafStruc(Falkor_2018_raw)

####  obs/in-situ/cruise/HOE_legacy_2A  #####
HOE_legacy_2A_raw = cruise_raw + 'HOE_legacy_2A/'
makedir(HOE_legacy_2A_raw)
nrt_HOE_legacy_2A_raw, rep_HOE_legacy_2A_raw, doc_HOE_legacy_2A_raw, code_HOE_legacy_2A_raw = leafStruc(HOE_legacy_2A_raw)

####  obs/in-situ/cruise/HOE_legacy_2B  #####
HOE_legacy_2B_raw = cruise_raw + 'HOE_legacy_2B/'
makedir(HOE_legacy_2B_raw)
nrt_HOE_legacy_2B_raw, rep_HOE_legacy_2B_raw, doc_HOE_legacy_2B_raw, code_HOE_legacy_2B_raw = leafStruc(HOE_legacy_2B_raw)

####  obs/in-situ/cruise/HOE_legacy_3  #####
HOE_legacy_3_raw = cruise_raw + 'HOE_legacy_3/'
makedir(HOE_legacy_3_raw)
nrt_HOE_legacy_3_raw, rep_HOE_legacy_3_raw, doc_HOE_legacy_3_raw, code_HOE_legacy_3_raw = leafStruc(HOE_legacy_3_raw)

####  obs/in-situ/cruise/HOE_legacy_4  #####
HOE_legacy_4_raw = cruise_raw + 'HOE_legacy_4/'
makedir(HOE_legacy_4_raw)
nrt_HOE_legacy_4_raw, rep_HOE_legacy_4_raw, doc_HOE_legacy_4_raw, code_HOE_legacy_4_raw = leafStruc(HOE_legacy_4_raw)

####  obs/in-situ/cruise/HOTLAVA  #####
HOTLAVA_raw = cruise_raw + 'HOTLAVA/'
makedir(HOTLAVA_raw)
nrt_HOTLAVA_raw, rep_HOTLAVA_raw, doc_HOTLAVA_raw, code_HOTLAVA_raw = leafStruc(HOTLAVA_raw)


####  obs/in-situ/cruise/HL2A_diel_metagenomicse  #####
HL2A_diel_metagenomics_raw = cruise_raw + 'HL2A_diel_metagenomics/'
makedir(HL2A_diel_metagenomics_raw)
nrt_HL2A_diel_metagenomics_raw, rep_HL2A_diel_metagenomics_raw, doc_HL2A_diel_metagenomics_raw, code_HL2A_diel_metagenomics_raw = leafStruc(HL2A_diel_metagenomics_raw)



####  obs/in-situ/cruise/gradients_1e  #####
gradients_1_raw = cruise_raw + 'gradients_1/'
makedir(gradients_1_raw)
nrt_gradients_1_raw, rep_gradients_1_raw, doc_gradients_1_raw, code_gradients_1_raw = leafStruc(gradients_1_raw)


####  obs/in-situ/cruise/gradients_2  #####
gradients_2_raw = cruise_raw + 'gradients_2/'
makedir(gradients_2_raw)
nrt_gradients_2_raw, rep_gradients_2_raw, doc_gradients_2_raw, code_gradients_2_raw = leafStruc(gradients_2_raw)

####  obs/in-situ/cruise/gradients_3  #####
gradients_3_raw = cruise_raw + 'gradients_3/'
makedir(gradients_3_raw)
nrt_gradients_3_raw, rep_gradients_3_raw, doc_gradients_3_raw, code_gradients_3_raw = leafStruc(gradients_3_raw)


####  obs/in-situ/cruise/HOT268  #####
HOT268_raw = cruise_raw + 'HOT268/'
makedir(HOT268_raw)
nrt_HOT268_raw, rep_HOT268_raw, doc_HOT268_raw, code_HOT268_raw = leafStruc(HOT268_raw)

####  obs/in-situ/cruise/allSeaFlowCruises  #####
allSeaFlowCruises_raw = cruise_raw + 'allSeaFlowCruises/'
makedir(allSeaFlowCruises_raw)
nrt_allSeaFlowCruises_raw, rep_allSeaFlowCruises_raw, doc_allSeaFlowCruises_raw, code_allSeaFlowCruises_raw = leafStruc(allSeaFlowCruises_raw)

####  obs/in-situ/cruise/AMT_cruises  #####
AMT_cruises_raw = cruise_raw + 'AMT_cruises/'
makedir(AMT_cruises_raw)
nrt_AMT_cruises_raw, rep_AMT_cruises_raw, doc_AMT_cruises_raw, code_AMT_cruises_raw = leafStruc(AMT_cruises_raw)

####  obs/in-situ/cruise/GLODAP  #####
GLODAP_raw = cruise_raw + 'GLODAP/'
makedir(GLODAP_raw)
nrt_GLODAP_raw, rep_GLODAP_raw, doc_GLODAP_raw, code_GLODAP_raw = leafStruc(GLODAP_raw)


####  obs/in-situ/cruise/GLODAP_gridded  #####
GLODAP_gridded_raw = cruise_raw + 'GLODAP_gridded/'
makedir(GLODAP_gridded_raw)
nrt_GLODAP_gridded_raw, rep_GLODAP_gridded_raw, doc_GLODAP_gridded_raw, code_GLODAP_gridded_raw = leafStruc(GLODAP_gridded_raw)

####  obs/in-situ/cruise/CPR_zooplankton   #####
CPR_zooplankton_raw = cruise_raw + 'CPR_zooplankton/'
makedir(CPR_zooplankton_raw)
nrt_CPR_zooplankton_raw, rep_CPR_zooplankton_raw, doc_CPR_zooplankton_raw, code_CPR_zooplankton_raw = leafStruc(CPR_zooplankton_raw)


#########  obs/in-situ/station  #########
station_raw = in_situ_raw + 'station/'
makedir(station_raw)
####  obs/in-situ/station/hot  #####
hot_raw = station_raw + 'hot/'
makedir(hot_raw)
nrt_hot_raw, rep_hot_raw, doc_hot_raw, code_hot_raw = leafStruc(hot_raw)

#########  obs/in-situ/float  #########
float_raw = in_situ_raw + 'float/'
makedir(float_raw)
####  obs/in-situ/float/argo  #####
argo_raw = float_raw + 'argo/'
makedir(argo_raw)
####  obs/in-situ/float/argo/index  #####
index_argo_raw = argo_raw + 'index/'
makedir(index_argo_raw)
####  obs/in-situ/float/argo/prof  #####
prof_argo_raw = argo_raw + 'prof/'
makedir(prof_argo_raw)
nrt_prof_argo_raw, rep_prof_argo_raw, doc_prof_argo_raw, code_prof_argo_raw = leafStruc(prof_argo_raw)
####  obs/in-situ/float/argo/traj  #####
traj_argo_raw = argo_raw + 'traj/'
makedir(traj_argo_raw)
nrt_traj_argo_raw, rep_traj_argo_raw, doc_traj_argo_raw, code_traj_argo_raw = leafStruc(traj_argo_raw)
####  obs/in-situ/float/argo/merge  #####
merge_argo_raw = argo_raw + 'merge/'
makedir(merge_argo_raw)
nrt_merge_argo_raw, rep_merge_argo_raw, doc_merge_argo_raw, code_merge_argo_raw = leafStruc(merge_argo_raw)




########  obs/remote/satellite  ########
satellite_raw = remote_raw + 'satellite/'
makedir(satellite_raw)

alt_raw = satellite_raw + 'alt/'
nrt_alt_raw, rep_alt_raw, doc_alt_raw, code_alt_raw = leafStruc(alt_raw)
nrt_alt_prefix = 'nrt_alt_'
rep_alt_prefix = 'rep_alt_'

sst_raw = satellite_raw + 'sst/'
nrt_sst_raw, rep_sst_raw, doc_sst_raw, code_sst_raw = leafStruc(sst_raw)
nrt_sst_prefix = 'nrt_sst_'
rep_sst_prefix = 'rep_sst_'

sss_raw = satellite_raw + 'sss/'
nrt_sss_raw, rep_sss_raw, doc_sss_raw, code_sss_raw = leafStruc(sss_raw)
nrt_sss_prefix = 'nrt_sss_'
rep_sss_prefix = 'rep_sss_'

chl_raw = satellite_raw +'chl/'
nrt_chl_raw, rep_chl_raw, doc_chl_raw, code_chl_raw = leafStruc(chl_raw)
nrt_chl_prefix = 'nrt_chl_'
rep_chl_prefix = 'rep_chl_'

chl_8day_raw = satellite_raw +'chl_8day/'
nrt_chl_8day_raw, rep_chl_8day_raw, doc_chl_8day_raw, code_chl_8day_raw = leafStruc(chl_8day_raw)
nrt_chl_8day_prefix = 'nrt_chl_8day_'
rep_chl_8day_prefix = 'rep_chl_8day_'

wind_raw = satellite_raw + 'wind/'
nrt_wind_raw, rep_wind_raw, doc_wind_raw, code_wind_raw = leafStruc(wind_raw)
nrt_wind_prefix = 'nrt_wind_'
rep_wind_prefix = 'rep_wind_'

ftle_bw_sla_raw = satellite_raw + 'ftle_bw_sla/'
nrt_ftle_bw_sla_raw, rep_ftle_bw_sla_raw, doc_ftle_bw_sla_raw, code_ftle_bw_sla_raw = leafStruc(ftle_bw_sla_raw)
nrt_ftle_bw_sla_prefix = 'nrt_ftle_bw_sla_'
rep_ftle_bw_sla_prefix = 'rep_ftle_bw_sla_'

ftle_fw_sla_raw = satellite_raw + 'ftle_fw_sla/'
nrt_ftle_fw_sla_raw, rep_ftle_fw_sla_raw, doc_ftle_fw_sla_raw, code_ftle_fw_sla_raw = leafStruc(ftle_fw_sla_raw)
nrt_ftle_fw_sla_prefix = 'nrt_ftle_fw_sla_'
rep_ftle_fw_sla_prefix = 'rep_ftle_fw_sla_'

ftle_bw_adt_raw = satellite_raw + 'ftle_bw_adt/'
nrt_ftle_bw_adt_raw, rep_ftle_bw_adt_raw, doc_ftle_bw_adt_raw, code_ftle_bw_adt_raw = leafStruc(ftle_bw_adt_raw)
nrt_ftle_bw_adt_prefix = 'nrt_ftle_bw_adt_'
rep_ftle_bw_adt_prefix = 'rep_ftle_bw_adt_'

ftle_fw_adt_raw = satellite_raw + 'ftle_fw_adt/'
nrt_ftle_fw_adt_raw, rep_ftle_fw_adt_raw, doc_ftle_fw_adt_raw, code_ftle_fw_adt_raw = leafStruc(ftle_fw_adt_raw)
nrt_ftle_fw_adt_prefix = 'nrt_ftle_fw_adt_'
rep_ftle_fw_adt_prefix = 'rep_ftle_fw_adt_'

vort_sla_raw = satellite_raw + 'vort_sla/'
nrt_vort_sla_raw, rep_vort_sla_raw, doc_vort_sla_raw, code_vort_sla_raw = leafStruc(vort_sla_raw)
nrt_vort_sla_prefix = 'nrt_vort_sla_'
rep_vort_sla_prefix = 'rep_vort_sla_'

vort_adt_raw = satellite_raw + 'vort_adt/'
nrt_vort_adt_raw, rep_vort_adt_raw, doc_vort_adt_raw, code_vort_adt_raw = leafStruc(vort_adt_raw)
nrt_vort_adt_prefix = 'nrt_vort_adt_'
rep_vort_adt_prefix = 'rep_vort_adt_'

armor3d_raw = satellite_raw + 'armor3d/'
nrt_armor3d_raw, rep_armor3d_raw, doc_armor3d_raw, code_armor3d_raw = leafStruc(armor3d_raw)
nrt_armor3d_prefix = 'nrt_armor3d_'
rep_armor3d_prefix = 'rep_armor3d_'

modis_aerosol_raw = satellite_raw + 'modis_aerosol/'
nrt_modis_aerosol_raw, rep_modis_aerosol_raw, doc_modis_aerosol_raw, code_modis_aerosol_raw = leafStruc(modis_aerosol_raw)
nrt_modis_aerosol_prefix = 'nrt_modis_aerosol_'
rep_modis_aerosol_prefix = 'rep_modis_aerosol_'

modis_sea_ice_raw = satellite_raw + 'modis_sea_ice/'
nrt_modis_sea_ice_raw, rep_modis_sea_ice_raw, doc_modis_sea_ice_raw, code_modis_sea_ice_raw = leafStruc(modis_sea_ice_raw)
nrt_modis_sea_ice_prefix = 'nrt_modis_sea_ice_'
rep_modis_sea_ice_prefix = 'rep_modis_sea_ice_'


col_raw = satellite_raw + 'col/'
nrt_col_raw, rep_col_raw, doc_col_raw, code_col_raw = leafStruc(col_raw)
nrt_col_RRS412_prefix = 'nrt_col_RRS412_'
nrt_col_RRS443_prefix = 'nrt_col_RRS443_'
nrt_col_RRS490_prefix = 'nrt_col_RRS490_'
nrt_col_RRS555_prefix = 'nrt_col_RRS555_'
nrt_col_RRS670_prefix = 'nrt_col_RRS670_'
nrt_col_CDM443_prefix = 'nrt_col_CDM443_'
nrt_col_BBP443_prefix = 'nrt_col_BBP443_'
nrt_col_KD490_prefix = 'nrt_col_KD490_'
nrt_col_ZSD_prefix = 'nrt_col_ZSD_'
nrt_col_SPM_prefix = 'nrt_col_SPM_'
rep_col_RRS412_prefix = 'rep_col_RRS412_'
rep_col_RRS443_prefix = 'rep_col_RRS443_'
rep_col_RRS490_prefix = 'rep_col_RRS490_'
rep_col_RRS555_prefix = 'rep_col_RRS555_'
rep_col_RRS670_prefix = 'rep_col_RRS670_'
rep_col_CDM443_prefix = 'rep_col_CDM443_'
rep_col_BBP443_prefix = 'rep_col_BBP443_'
rep_col_KD490_prefix = 'rep_col_KD490_'
rep_col_ZSD_prefix = 'rep_col_ZSD_'
rep_col_SPM_prefix = 'rep_col_SPM_'
