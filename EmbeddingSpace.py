import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential , Model
from tensorflow.keras.layers import Embedding, GlobalAveragePooling1D,Dense

src='D:/MUSIC/Experiment1/Data/all_middle_columns.txt'
df = pd.read_csv(src, header=None)
unique_values = df[0].unique()

one_hot_encoding = pd.get_dummies(df[0], prefix='one_hot')
one_hot_array = one_hot_encoding.to_numpy()
print(len(one_hot_array)) 

result_df = pd.DataFrame({
    'number': df[0],
    'one_hot_array': list(one_hot_array)
})

# Deep Autoencoder Model
model = Sequential()
model.add(Dense(128, activation='relu', input_dim=36))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(20, activation='linear'))   # Compressed Representation
model.add(Dense(32, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(36, activation='linear'))  # Output layer (Reconstruction)

model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

history = model.fit(one_hot_array, one_hot_array, epochs=3, batch_size=2048, validation_split=0.2)

encoder_model = Model(inputs=model.input, outputs=model.layers[3].output)  

compressed_representation = encoder_model.predict(one_hot_array)

