#! /bin/sh

module load bedtools

multiIntersectBed -wo -i DMIR_sorted.bed DPER_sorted.bed DPSE_AFC14_sorted.bed DPSE_AFC19_sorted.bed DPSE_AFC24_sorted.bed DPSE_AFC30_sorted.bed DPSE_AFC47_sorted.bed DPSE_AFC48_sorted.bed DPSE_AFC49_sorted.bed DPSE_AFC56_sorted.bed DPSE_AFC57_sorted.bed DPSE_AFC60_sorted.bed DPSE_Cirulli_sorted.bed DPSE_Flagstaff_sorted.bed DPSE_FlagstaffUtraFine_sorted.bed DPSE_Kulathinal_sorted.bed DPSE_MC13_sorted.bed DPSE_MC14_sorted.bed DPSE_MC15_sorted.bed DPSE_MC17_sorted.bed DPSE_MC20_sorted.bed DPSE_MC27_sorted.bed DPSE_MC6_sorted.bed DPSE_Pikespeak_sorted.bed -header -names DMIR DPER DPSE_AFC14 DPSE_AFC19 DPSE_AFC24 DPSE_AFC30 DPSE_AFC47 DPSE_AFC48 DPSE_AFC49 DPSE_AFC56 DPSE_AFC57 DPSE_AFC60 DPSE_Cirulli DPSE_Flagstaff DPSE_FlagstaffUtraFine DPSE_Kulathinal DPSE_MC13 DPSE_MC14 DPSE_MC15 DPSE_MC17 DPSE_MC20 DPSE_MC27 DPSE_MC6 DPSE_Pikespeak > BedAll.bed
echo "Finished"
