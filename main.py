from wds_read_text import wds_read_files
from gaia_read_excel import gaia_read_excel_file
import pandas as pd
from pdf import BuildPDF



wds, wds_indexes = wds_read_files('data')
gaia = gaia_read_excel_file('data/Résultats-J-GaiaDR3.xlsx')
pdf = BuildPDF('tableau.pdf')



for name in gaia['Name'].unique().tolist():
    ref = wds_indexes[name] if name in wds_indexes else "REF UNKNOWN"
    if ref!="REF UNKNOWN":
        gaia_primary = gaia.loc[(gaia['Name'] == name) & (gaia['Rho (arcsec)'] == 0)]
        if len(gaia_primary)>0:
            gaia_primary = gaia_primary.iloc[0]
            gaia_secondary = gaia.loc[(gaia['Name'] == name) & (gaia['Rho (arcsec)'] != 0)]
            if len(gaia_secondary)>0:
                gaia_secondary = gaia_secondary.iloc[0]
                ad = str(gaia_primary["ra"])
                dec = str(gaia_primary["dec"])
                ref_g = str(gaia_primary["#source_id"])
                m1 = str(round(float(gaia_primary["phot_g_mean_mag"]),2))
                m2 = str(round(float(gaia_secondary["phot_g_mean_mag"]),2))

                parallax =  str(round(gaia_primary["parallax"],2))
                proper_mvt = str(round(gaia_primary["pmra"],2))
                rad_velocity = str(round(gaia_primary["radial_velocity"],2))
                dist = str(round(gaia_primary["dist"],2))


                pdf.add_double_stars_page(wds, name, ref, ad, dec, ref_g, m1, m2, parallax, proper_mvt, rad_velocity, dist)
                
pdf.save()