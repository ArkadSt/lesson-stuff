

document.addEventListener('DOMContentLoaded', function() {
    const slider = document.getElementById('slider');
    let isDown = false;
    let startX;
    let scrollLeft;
    let slideWidth;
    
    // Calculate slide width
    function calculateSlideWidth() {
        const slide = slider.querySelector('.slide');
        slideWidth = slide.offsetWidth + (slide.offsetWidth * 0.03); // Width + margin
    }

    calculateSlideWidth();
    window.addEventListener('resize', calculateSlideWidth);
    
    // Mouse events
    slider.addEventListener('mousedown', (e) => {
        isDown = true;
        slider.style.transition = 'none';
        slider.style.cursor = 'grabbing';
        startX = e.pageX - slider.offsetLeft;
        scrollLeft = slider.scrollLeft;
        e.preventDefault();
    });
    
    slider.addEventListener('mouseleave', () => {
        isDown = false;
        snapToSlide();
    });
    
    slider.addEventListener('mouseup', () => {
        isDown = false;
        snapToSlide();
    });
    
    slider.addEventListener('mousemove', (e) => {
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - slider.offsetLeft;
        const walk = (x - startX);
        const currentTranslate = -walk + scrollLeft;
        slider.style.transform = `translateX(${-currentTranslate}px)`;
    });
    
    // Touch events
    slider.addEventListener('touchstart', (e) => {
        isDown = true;
        slider.style.transition = 'none';
        startX = e.touches[0].pageX - slider.offsetLeft;
        scrollLeft = slider.scrollLeft;
    });
    
    slider.addEventListener('touchend', () => {
        isDown = false;
        snapToSlide();
    });
    
    slider.addEventListener('touchmove', (e) => {
        if (!isDown) return;
        const x = e.touches[0].pageX - slider.offsetLeft;
        const walk = (x - startX);
        const currentTranslate = -walk + scrollLeft;
        slider.style.transform = `translateX(${-currentTranslate}px)`;
        e.preventDefault(); // Prevent page scrolling
    });
    
    // Function to snap to nearest slide
    function snapToSlide() {
        slider.style.transition = 'transform 0.3s ease';
        
        // Get current transform value
        const style = window.getComputedStyle(slider);
        const matrix = new WebKitCSSMatrix(style.transform);
        const currentTranslateX = matrix.m41;
        
        // Calculate closest slide
        const slideIndex = Math.round(Math.abs(currentTranslateX) / slideWidth);
        const newTranslateX = slideIndex * slideWidth;
        
        // Don't allow scrolling past the last slide
        const maxTranslate = (slider.children.length - 1) * slideWidth;
        const limitedTranslate = Math.min(newTranslateX, maxTranslate);
        
        slider.style.transform = `translateX(${-limitedTranslate}px)`;
        slider.style.cursor = 'grab';
    }
});