#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
#Load dataset
dataset = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/retail_raw_reduced.csv')
print('Ukuran dataset: %d baris dan %d kolom\n' % dataset.shape)
print('Lima data teratas\n',dataset.head())


# In[ ]:


#Keterngan variable
#order_id : ID dari order/transaksi, 1 transaksi bisa terdiri dari beberapa produk, tetapi hanya dilakukan oleh 1 customer
#order_date : tanggal terjadinya transaksi
#customer_id : ID dari pembeli, bisa jadi dalam satu hari, 1 customer melakukan transaksi beberapa kali
#city : kota tempat toko terjadinya transaksi
#province :  provinsi (berdasarkan city)
#product_id : ID dari suatu product yang dibeli
#brand : brand/merk dari product. Suatu product yang sama pasti memiliki brand yang sama
#quantity : Kuantitas / banyaknya product yang dibeli
#item_price : Harga dari 1 product (dalam Rupiah). Suatu product yang sama, bisa jadi memiliki harga yang berbeda saat dibeli


# In[3]:


#Penambahan kolom order month pada dataset
import datetime
#menambahkan kolom baru order_month berdasarkan kolom order_date
dataset['order_month']=dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x,'%Y-%m-%d').strftime('%Y-%m'))
print('Dataset dengan kolom order_month:\n',dataset.head())
print(dataset.shape)


# In[4]:


#Penambahan kolom GMV pada Dataset
#alternatif membuta kolom baru selain menggunakan apply lambda
dataset['gmv']=dataset['item_price']*dataset['quantity']
print('Ukuran dataset: %d baris %d kolom\n' % dataset.shape)
print(dataset.head())


# In[5]:


#Membuat data agregrat
monthly_amount = dataset.groupby('order_month')['gmv'].sum().reset_index()
print('Data Monthly amounth:\n',monthly_amount)


# In[6]:


#PLOT 
#membuat linechart trend pertumbuhan GMV
#definisikan order_month di sumbu x dan gmv di sumbu y
import matplotlib.pyplot as plt
#plt.plot(x,y)
plt.plot(monthly_amount['order_month'],monthly_amount['gmv'])
plt.show()


# In[20]:


#plot tanpa pendekatan dengan variabel baru
dataset.groupby(['order_month'])['gmv'].sum().plot()
plt.show()


# In[43]:


#Kustomisasi grafik
#https://matplotlib.org/3.1.3/gallery/showcase/anatomy.html.
#Mengubah ukuran
fig=plt.figure(figsize=(15,5))
plt.plot(monthly_amount['order_month'],monthly_amount['gmv'],color='red',
      marker='o',linestyle='-.',linewidth=2)

#menambahkan title dan axis label
plt.title('Monthly GMV Year 2019',loc='left',pad=35,fontsize=22,color='red')
#loc : lokasi, pad: jarak title dgn grafik
plt.xlabel('Order month',fontsize=17)
plt.ylabel('Total GMV(in Billions)',fontsize=17)
#Menambahkan grid > untuk memudahkan plotting ke sumbu y
plt.grid(color='blue',linestyle=':',linewidth=3)
#kustomisasi axis ticks
#menentukan batas minimum dan maksimum axis ticks
plt.ylim(ymin=0)#memulai sumbu y dari 0
labels,locatios=plt.yticks()
#nilai awal dibagi 1 milliyar
plt.yticks(labels,(labels/1000000000).astype(int))
#Menambhakan informasi pada plot
plt.text(0.45,0.72, 'The GMV Increased significantly on October 2019',
         transform=fig.transFigure,color='black',fontsize=20)
plt.savefig('monthly_gmv.png')
plt.show()


# In[44]:


#Menyimpan hasil plot menjadi file image
plt.savefig('monthly_gmv.png',quality=95)
#Pengaturan parameter untuk menyimpan gambar
#dpi : resolusi gambar (dots per inch)
#quality : kualitas gambar (hanya berlaku untuk yg berformat jpg/jpeg), bisa diisi 1 (paling buruk) hingga 95 (paling bagus)
#facecolor : memberikan warna pada bagian depan figure, di luar area plot
#edgecolor : memberikan warna pada pinggiran gambar
#transparent : True (gambarmenjadi transparan (jika fileny png))


# In[ ]:


databaru = pd.read_csv(''https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/retail_raw_reduced.csv')

