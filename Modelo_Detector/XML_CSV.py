import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text),
                     member[0].text,
                     )
            xml_list.append(value)
    column_name = ['filename', 'xmin','ymin','xmax', 'ymax', 'class']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df

dataset_df = xml_to_csv(os.path.abspath(os.getcwd())+"/imagenes")

print("Completado!!")


import skimage.io as io
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import matplotlib.patches as patches


print(dataset_df)

def showObjects(image_df):

    img_path = image_df.filename

    image = io.imread(img_path)
    draw = image.copy()
    
    # Create figure and axes
    fig,ax = plt.subplots(1)
    ax.imshow(draw)
    rect = patches.Rectangle((image_df.xmin,image_df.ymin),image_df.xmax-image_df.xmin,image_df.ymax-image_df.ymin,linewidth=1,edgecolor='r',facecolor='none')

    plt.axis('off')
    ax.add_patch(rect)
    plt.show()

showObjects(dataset_df.iloc[2])
   
   
# DIVIDIR DATASET
train_df, test_df = train_test_split(
  dataset_df, 
  test_size=0.2, 
  random_state=2
)

# CREAR ARCHIVOS CSV
train_df.to_csv('dataset.csv', index=False, header=None)
test_df.to_csv('dataset_test.csv', index=False, header=None)

classes = set(['hand'])

with open('dataset.csv', 'w') as f:
    for i, line in enumerate(sorted(classes)):
        f.write('{},{}\n'.format(line,i))
