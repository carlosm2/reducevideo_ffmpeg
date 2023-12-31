import ffmpeg # importa libreria ffmpeg, entonces se tiene que instalar antes

def reduce_video_size(input_file, output_file, codec='libx264', crf=23, preset='medium', tune=None):
    try:
        ffmpeg.input(input_file).output(output_file, codec=codec, crf=
        print(f"Video successfully compressed to {output_file}")
    except ffmpeg.Error as e:
        print(f"Error: {e.stderr}")
        raise

if __name__ == "__main__":
    input_file = "input_video.mp4"  # Reemplaza con la ruta de tu archivo de video de entrada
    output_file = "output_video.mp4"  # Reemplaza con la ruta deseada para el archivo de salida
    codec = 'libx264'  # Códec de video a utilizar (libx264 es ampliamente compatible y eficiente)
    crf_value = 23  # Ajusta el valor CRF (Constant Rate Factor) para controlar la compresión
    preset = 'medium'  # Preset de compresión ('slow', 'medium', 'fast')
    tune = None  # Puedes especificar una opción de sintonización para el códec (opcional)

    reduce_video_size(input_file, output_file, codec=codec, crf=crf_value, preset=preset, tune=tune)
