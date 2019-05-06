#! /usr/bin/env python3

import vcf

__author__ = 'Gerry'


class Assignment2:
    
    def __init__(self):
        ## Check if pyvcf is installed
        print("PyVCF version: %s" % vcf.VERSION)
        

    def get_average_quality_of_file(self):
        '''
        Get the average PHRED quality of all variants
        :return:
        '''    
        print("TODO")
        
        
    def get_total_number_of_variants_of_file(self):
        '''
        Get the total number of variants
        :return: total number of variants
        '''
        #grep '^chr22' chr22.vcf | wc -l
        v_counter = 0
        with open("chr22.vcf") as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)
            for record in vcf_reader:
                v_counter +=  1
        return(v_counter)
        #print("Total Number of Variants: ", v_counter)
    
    
    def get_variant_caller_of_vcf(self):            # NICHT vorahnden -- HILFE!
        '''
        Return the variant caller name
        :return: 
        '''
        print("TODO")
        
        
    def get_human_reference_version(self):    # HILFE ---Funktioniert  nicht
        '''
        Return the genome reference version
        :return: 
        '''
        snv_counter = 0
        with open("chr22.vcf") as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)
            for record in vcf_reader:
                if record.is_snp:
                    snv_counter = snv_counter + 1
        #return(snv_counter)
        print("Number of snv: ", snv_counter)

        print("TODO")
        
        
    def get_number_of_indels(self):
        '''
        Return the number of identified INDELs
        :return:
        '''
        indel_counter = 0
        with open("chr22.vcf") as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)
            for record in vcf_reader:
                if record.is_indel:
                    indel_counter +=  1
        return(indel_counter)


        #print("TODO")
        

    def get_number_of_snvs(self):
        '''
        Return the number of SNVs
        :return: 
        ''' 
        snv_counter = 0
        with open("chr22.vcf") as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)
            for record in vcf_reader:
                if record.is_snp:
                    snv_counter = snv_counter + 1
        return(snv_counter)
        #print("Number of snv: ", snv_counter)
        
    def get_number_of_heterozygous_variants(self):
        '''
        Return the number of heterozygous variants
        :return: 
        '''
        
        with open("chr22.vcf") as my_vcf_fh:
            het_counter = 0
            vcf_reader = vcf.Reader(my_vcf_fh)
            for record in vcf_reader:
                if record.num_het:
                    het_counter += 1

            #return(vcf_reader.num_het)

        return(het_counter)
        #print("TODO")
        
    
    def merge_chrs_into_one_vcf(self):
        '''
        Creates one VCF containing all variants of chr21 and chr22
        :return:
        '''

        file = open("chr21.vcf") 
        w_f = open("newfile1.vcf", "w+") 
        for line in file: 
            
            w_f.write(line)
        file.close
        w_f.close

        file = open("chr22.vcf") 
        w_f = open("newfile1.vcf", "a") 
        for line in file: 
            w_f.write(line)
        file.close
        w_f.close

        #print("TODO")
        
        #print("Number of total variants")
        
    
    def print_summary(self):
        #print("Total Number of Variants: ", self.get_total_number_of_variants_of_file())
        #print("Number of INDELs", self.get_number_of_indels())
        #print("Number of SNVS: ", self.get_number_of_snvs())
        #print("Number of Heterozygous Variants: ", self.get_number_of_heterozygous_variants())
        print("lines here: " , self.merge_chrs_into_one_vcf())
    
    
def main():
    print("Assignment 2")
    assignment2 = Assignment2()
    assignment2.print_summary()
    print("Done with assignment 2")
        
        
if __name__ == '__main__':
    main()
   
    



