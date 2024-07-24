    """
    with st.expander("Generate Artwork", expanded=False):
        prompt_text = text_area
        art_style = st.selectbox("Choose an Image Style", [
            "Abstract", "Cute", "Fantasy", "Futuristic", "Realistic",
            "Science Fiction", "Surreal", "Techno"
        ])
        st.subheader("Your artwork will take a moment. Please be patient.")
        if st.button("Generate Artwork"):
            artwork_image = generate_image(prompt_text, art_style)
            if artwork_image:
                st.image(artwork_image, width=400)
            else:
                st.error("Error generating image. Please try again.")
    """