#! /bin/sh

module load bedtools

multiIntersectBed -wo -i DMIR.csv DPER.csv DPSE_AFC14.csv DPSE_AFC19.csv DPSE_AFC24.csv DPSE_AFC30.csv DPSE_AFC47.csv DPSE_AFC48.csv DPSE_AFC49.csv DPSE_AFC56.csv DPSE_AFC57.csv DPSE_AFC60.csv DPSE_Cirulli.csv DPSE_Flagstaff.csv DPSE_FlagstaffUtraFine.csv DPSE_Kulathinal.csv DPSE_MC13.csv DPSE_MC14.csv DPSE_MC15.csv DPSE_MC17.csv DPSE_MC20.csv DPSE_MC27.csv DPSE_MC6.csv DPSE_Pikespeak.csv -header -names DMIR DPER DPSE_AFC14 DPSE_AFC19 DPSE_AFC24 DPSE_AFC30 DPSE_AFC47 DPSE_AFC48 DPSE_AFC49 DPSE_AFC56 DPSE_AFC57 DPSE_AFC60 DPSE_Cirulli DPSE_Flagstaff DPSE_FlagstaffUltrafine DPSEKulathinal DPSE_MC13 DPSE_MC14 DPSE_MC15 DPSE_MC17 DPSE_MC20 DPSE_MC27 DPSE_MC6 DPSE_PikesPeak > Bed_all

echo "Finished""
done
