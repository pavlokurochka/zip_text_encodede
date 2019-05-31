#%%
import base64 
import argparse
#%%
def zip2txt(filename):

    with open(f'{filename}.zip', 'rb') as image: 
        image_read = image.read() 
        coding_result = base64.b64encode(image_read).decode('utf-8')
        
        with open(f'{filename}.txt', 'w') as textfile:
            textfile.write(coding_result)  

#%%
def txt2zip(filename):
    with open(f'{filename}.txt', 'rt') as textfile: 
        text_read = textfile.read() 
        coding_result = base64.b64decode(text_read.encode('utf-8'))
        
        with open(f'{filename}.zip', 'wb') as image:
            image.write(coding_result)  


#%%
def main():
    parser = argparse.ArgumentParser(
        description='Encode/decode zip/txt')
    parser.add_argument(dest='filename', type=str,
                        help="File to process. Must be zip or txt. ")
    args = parser.parse_args()
    basename = args.filename.split('.')[0]
    extension = args.filename.split('.')[1]
    
    if extension =='zip':
        zip2txt(basename)
        print(f'Encoded {basename}.txt')
    else:
        txt2zip(basename)
        print(f'Decoded {basename}.zip')
 
                

if __name__ == "__main__":
    import timing
    main() 