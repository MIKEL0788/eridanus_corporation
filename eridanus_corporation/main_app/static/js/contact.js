// Animation et interactivité pour la page Contact
document.addEventListener('DOMContentLoaded', function() {
    console.log('Page Contact chargée !');
    
    // Animation des cartes au scroll
    const infoCards = document.querySelectorAll('.info-card');
    
    const observerOptions = {
        threshold: 0.2,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.style.opacity = '0';
                    entry.target.style.transform = 'translateX(-30px)';
                    
                    setTimeout(() => {
                        entry.target.style.transition = 'all 0.5s ease';
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateX(0)';
                    }, 50);
                }, index * 100);
                
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    infoCards.forEach(card => {
        observer.observe(card);
    });
    
    // Animation du bouton CTA
    const ctaButton = document.querySelector('.btn-primary');
    if (ctaButton) {
        ctaButton.addEventListener('click', function(e) {
            e.preventDefault();
            alert('Le formulaire de contact sera disponible bientôt (géré par Yakoub) !');
        });
    }
    
    // Effet hover sur les cartes
    infoCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.background = 'linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.background = '#f8f9fa';
        });
    });
});