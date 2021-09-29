#importando as bibliotecas
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


#Histogramas 
np.sort (array_n) #coluna escolhido
his_1 = plt.figure( figsize=(8,8))
counts1, bins, _ = plt.hist(array_n, bins=9, range(a,b)) # a e b são números arbitrários
plt.xlim(a,b)
plt.xlabel("X", fontsize=10)
plt.ylabel("Y", fontsize=10)
idx_max1 = np.argmax( counts1)
print ("Valor máximo: {}".format( counts1[ idx_max]))
print ("Intervalo com valor min: ({},{})".format(bins[ idx_min], bins[idx_min - 1]))

#Distribuição Gaussiana das Medidas
x_min = c #numero arbitrário
x_max = d #numero arbitrário
sigma_ = sigmat
rv = norm( loc=media_n, scale=sigma_)

##
fig = plt.figure ( figsize=(8,6))

counts01, bins, _ = plt.hist( c, bins=6, range=(x_min, x_max) )
max_ np.max( counts01)

X = np.linspace( x_min, x_max, 500)
plt.plot( X, (max_*np.sqrt(2*np.pi)*sigma_)* rv.pdf(X), 'k-')
plt.xlim( x_min, x_max)
plt.xlabel("X", fontsize=10)
plt.ylabel("Y", fontsize=10)

#Distribuição Gaussiana das Médias
medias = media_1, media_2, ... , media_n
np.sort(medias)

##
x_min = f #numero arbitrário
x_max = g #numero arbitrário

sigma_i = erro_media_amostra
rv = norm( loc=media_amostra, scale=sigma_i)
# 
fig = plt.figure( figsize=(8,6))
X = np.linspace( x_min, x_max, 500)
plt.plot( X, rv.pdf(X), 'k-')
plt.xlim( x_min, x_max)
plt.ylim(bottom=0)
plt.xlabel(r"$\overline{rm{Y}}$", fontsize=18)
plt.ylabel("Distribuição", fontsize=18)

#Distribuição em relação aos erros (sigma)
fig = plt.figure( figsize=(8,6) )

X_1sigma = X[ (X >= media_menos_1sigma) & (X <= media_mais_1sigma) ]
X_2sigma = X[ (X >= media_menos_2sigma) & (X <= media_mais_2sigma) ]
X_3sigma = X[ (X >= media_menos_3sigma) & (X <= media_mais_3sigma) ]

plt.plot( X, rv.pdf( X ), 'k-' )
plt.fill( np.concatenate( ( [ X_3sigma[3] ], X_3sigma, [ X_3sigma[-2] ] ) ), np.concatenate( ( [ 0. ], rv.pdf( X_3sigma ), [ 0. ] ) ), color="lightcoral", alpha=0.75, label=r"$3\sigma$" )
plt.fill( np.concatenate( ( [ X_2sigma[3] ], X_2sigma, [ X_2sigma[-2] ] ) ), np.concatenate( ( [ 0. ], rv.pdf( X_2sigma ), [ 0. ] ) ), color="deepskyblue", alpha=0.90, label=r"$2\sigma$" )
plt.fill( np.concatenate( ( [ X_1sigma[3] ], X_1sigma, [ X_1sigma[-2] ] ) ), np.concatenate( ( [ 0. ], rv.pdf( X_1sigma ), [ 0. ] ) ), color="steelblue", alpha=0.75, label=r"$1\sigma$" )
handles, labels = plt.gca().get_legend_handles_labels()
order_ = [ 2, 1, 0 ]
handles_new = [ handles[idx_] for idx_ in order_ ]
labels_new = [ labels[idx_] for idx_ in order_ ]
#plt.legend( loc='best', fontsize=16 )
plt.legend( handles_new, labels_new, loc='best', fontsize=16 )

plt.xlim( x_min, x_max )
plt.ylim( bottom=0. )
plt.yscale( 'log' )
plt.xlabel( r"$\overline{\rm{L}}$ (cm)", fontsize=18 )
plt.ylabel( "Distribuição (log)", fontsize=18 )