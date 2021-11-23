#! /bin/sh

module load bedtools

multiIntersectBed -wo -i DMIR.bed DPER.bed DPSE_AFC14.bed DPSE_AFC19.bed DPSE_AFC24.bed DPSE_AFC30.bed DPSE_AFC47.bed DPSE_AFC48.bed DPSE_AFC49.bed DPSE_AFC56.bed DPSE_AFC57.bed DPSE_AFC60.bed DPSE_Cirulli.bed DPSE_Flagstaff.bed DPSE_FlagstaffUtraFine.bed DPSE_Kulathinal.bed DPSE_MC13.bed DPSE_MC14.bed DPSE_MC15.bed DPSE_MC17.bed DPSE_MC20.bed DPSE_MC27.bed DPSE_MC6.bed DPSE_Pikespeak.bed -header -names DMIR DPER DPSE_AFC14 DPSE_AFC19 DPSE_AFC24 DPSE_AFC30 DPSE_AFC47 DPSE_AFC48 DPSE_AFC49 DPSE_AFC56 DPSE_AFC57 DPSE_AFC60 DPSE_Cirulli DPSE_Flagstaff DPSE_FlagstaffUtraFine DPSE_Kulathinal DPSE_MC13 DPSE_MC14 DPSE_MC15 DPSE_MC17 DPSE_MC20 DPSE_MC27 DPSE_MC6 DPSE_Pikespeak > BedAll.bed
echo "Finished""
done
