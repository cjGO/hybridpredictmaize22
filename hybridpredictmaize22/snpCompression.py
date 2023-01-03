# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_snpCompression.ipynb.

# %% auto 0
__all__ = ['vcf2numpy', 'SNP_PCA', 'SNP_evensample']

# %% ../nbs/01_snpCompression.ipynb 5
def vcf2numpy(vcf:str,chr:int):
    """
  in:
  vcf -> file.vcf
  chr -> chr (to be pulled)

  returns the allele dosage (0, 0.5, 1) for all hybrids
    """
    chr = str(chr)
    callset = allel.read_vcf(vcf, region=chr)
    chr_call = callset['calldata/GT']
    chr_alleles = np.sum(chr_call,axis=2)
    chr_alleles = chr_alleles/2

    return callset['samples'],chr_alleles


# %% ../nbs/01_snpCompression.ipynb 7
def SNP_PCA(vcfFile, foldername='./PC/', pc=10):
    """
    Input:
        foldername : storage location of npy arrays
        pc (int: # of pcs per chromosome)
        vcfFile (path)
    """
    chr_lens = []
    chr_pcs = []
    foldername = f'PCS_{pc}'
    if not os.path.exists(foldername):os.mkdir(foldername)
    for i in tqdm(range(1,11)):
      strain,chr = vcf2numpy(vcfFile, chr=i)
      pca = PCA(n_components=pc)
      pca.fit(chr)

      chr_len = chr.shape[0]
      chr_pc = pca.explained_variance_ratio_

      chr_lens.append(chr_len)
      chr_pcs.append(chr_pc)

      np.save(f'./{foldername}/Chr{str(i).zfill(3)}_pcs{pc}.npy', np.array([strain,pca.components_]))


# %% ../nbs/01_snpCompression.ipynb 8
def SNP_evensample(snps=50):
    """
    Input:
        foldername : storage location of npy arrays
        snps (int: # of snps sampled per chromosome)
        vcfFile (path)
    """
    for i in tqdm(range(1,11)):
      strain,chr = vcf2numpy('5_Genotype_Data_All_Years.vcf', chr=i)
      total_snps = chr.shape[0]

      for select_count in [10,50,100]:
        selected_snps = np.around(np.linspace(2,total_snps-1,select_count),decimals=0)
        kept_snps = []
        foldername = f'EVEN_{select_count}'
        if not os.path.exists(foldername):os.mkdir(foldername)

        for snp in selected_snps:
          kept_snps.append(chr[int(snp)])
        kept_snps = np.vstack(kept_snps)  
        np.save(f'./{foldername}/Chr{str(i).zfill(3)}_snps{select_count}.npy',np.array([strain,kept_snps]))

