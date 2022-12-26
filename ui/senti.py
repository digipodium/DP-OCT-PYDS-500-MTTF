import streamlit as st
from PIL import Image, ImageFilter

# Let the user select an image file
image_file = st.file_uploader('Upload image')

# Load the image and display it
if image_file:
    image = Image.open(image_file)
    st.image(image, caption='Original image', use_column_width=True)

    # Crop the image
    left = st.sidebar.slider('Left', 0, image.width, 0)
    top = st.sidebar.slider('Top', 0, image.height, 0)
    right = st.sidebar.slider('Right', left, image.width, image.width)
    bottom = st.sidebar.slider('Bottom', top, image.height, image.height)

    cropped_image = image.crop((left, top, right, bottom))

    # Display the cropped image
    st.image(cropped_image, caption='Cropped image', use_column_width=True)
    # Apply a filter to the image
    image_filter = st.sidebar.selectbox(
        'Filter',
        ['BLUR', 'CONTOUR', 'DETAIL', 'EDGE_ENHANCE', 'EDGE_ENHANCE_MORE', 'EMBOSS', 'FIND_EDGES', 'SHARPEN', 'SMOOTH', 'SMOOTH_MORE']
    )

    if image_filter:
        if image_filter == 'BLUR':
            filtered_image = image.filter(ImageFilter.BLUR)
        elif image_filter == 'CONTOUR':
            filtered_image = image.filter(ImageFilter.CONTOUR)
        elif image_filter == 'DETAIL':
            filtered_image = image.filter(ImageFilter.DETAIL)
        elif image_filter == 'EDGE_ENHANCE':
            filtered_image = image.filter(ImageFilter.EDGE_ENHANCE)
        elif image_filter == 'EDGE_ENHANCE_MORE':
            filtered_image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
        elif image_filter == 'EMBOSS':
            filtered_image = image.filter(ImageFilter.EMBOSS)
        elif image_filter == 'FIND_EDGES':
            filtered_image = image.filter(ImageFilter.FIND_EDGES)
        elif image_filter == 'SHARPEN':
            filtered_image = image.filter(ImageFilter.SHARPEN)
        elif image_filter == 'SMOOTH':
            filtered_image = image.filter(ImageFilter.SMOOTH)
        elif image_filter == 'SMOOTH_MORE':
            filtered_image = image.filter(ImageFilter.SMOOTH_MORE)

    # Display the modified image
    if cropped_image:
        st.image(cropped_image, caption='Cropped image', use_column_width=True)
    elif filtered_image:
        st.image(filtered_image, caption='Filtered image', use_column_width=True)
    else:
        st.image(image, caption='Original image', use_column_width=True)