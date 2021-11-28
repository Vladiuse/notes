console.log('js')
class Modal {
    constructor(el) {
      this.el = el;
      this.init();
    }
    
    init() {
      makeElementsUntabbable(this.el);
      
      // Open Modal
      document.querySelector('[data-module-init*="modal"]').addEventListener('click', () => {
        makeElementsTabbable(this.el);
        document.body.classList.add('modal-open');
        this.el.removeAttribute('aria-hidden');
        document.querySelector('.wrapper-modal').setAttribute('aria-hidden', 'true');
        document.querySelector('[data-module*="modal"]').style.display = 'block';
        trapTabWithinPopup(this.el);
      });
      function stopDefAction(evt) {
        evt.preventDefault();
    }
    
      // click success button
      document.getElementById('click-button').addEventListener('click', e => {
        var one = document.getElementById('input-1').value
        var two = document.getElementById('input-2').value
        
        console.log(one.length, two.length)
        // disable form
        if (one.length * two.length != 0){
          document.getElementById('register').addEventListener(
            'click', stopDefAction, false
          );
          //  подмена контента
          document.getElementById('register').hidden = true
          document.getElementById('modal-btn-open').hidden = true
          document.getElementById('success-card').style.display = 'block'
          window.setTimeout(function(){
            // close  
            const modal = document.querySelector('[data-module*="modal"]');
            const backdrop = document.querySelector('[data-modal-backdrop]');
            const content = document.querySelector('[data-modal-content]');
        
            backdrop.style.animation = 'fadeout 0.3s 0.3s';
            content.style.animation = 'fadeout 0.5s';
            
            makeElementsUntabbableAndFocusOnTrigger(modal, document.querySelector('[data-module-init="modal"]'))
        
            backdrop.addEventListener('animationend', function _removeModal() {
              document.body.classList.remove("modal-open");
              modal.setAttribute('aria-hidden', 'true');
              document.querySelector('.wrapper-modal').removeAttribute('aria-hidden');
              modal.style.display = 'none'
              backdrop.style.animation = '';
              content.style.animation = '';
              backdrop.removeEventListener('animationend', _removeModal);
            }); 
            // close
             }, 1000);

        }
        
      });

      // Close Modal with button or clicking outside modal
      document.querySelector('body').addEventListener('click', e => {
        if (e.target.hasAttribute('data-modal-close')) {
          this.closeModal();
        }
      });
      
      document.addEventListener('keydown', e => {
        if (document.body.classList.contains('modal-open') === false) return
        
        // Close Modal with esc key
        if (e.key === 'Escape') {
          this.closeModal();
        }
  
        // Prevent form submit while checkbox is focused
        if (e.key === 'Enter') {
          if (document.activeElement.getAttribute('type') === 'checkbox') {
            e.preventDefault();
            document.activeElement.toggleAttribute('checked');
          }
        }
      });
    }
    
    closeModal() {
      const modal = document.querySelector('[data-module*="modal"]');
      const backdrop = document.querySelector('[data-modal-backdrop]');
      const content = document.querySelector('[data-modal-content]');
  
      backdrop.style.animation = 'fadeout 0.3s 0.3s';
      content.style.animation = 'fadeout 0.5s';
      
      makeElementsUntabbableAndFocusOnTrigger(modal, document.querySelector('[data-module-init="modal"]'))
  
      backdrop.addEventListener('animationend', function _removeModal() {
        document.body.classList.remove("modal-open");
        modal.setAttribute('aria-hidden', 'true');
        document.querySelector('.wrapper-modal').removeAttribute('aria-hidden');
        modal.style.display = 'none'
        backdrop.style.animation = '';
        content.style.animation = '';
        backdrop.removeEventListener('animationend', _removeModal);
      });
  
    }
  }
   
  // Tab trapper - this is an a11y feature for keyboard users
  const getAllTabbableElements = [
    'a[href]',
    'button:not([disabled]):not([aria-hidden])',
    'input:not([disabled]):not([type="hidden"]):not([aria-hidden])',
    '[tabindex]:not([tabindex^="-"])'
  ];
  let tabbableElementsArray;
  let lastTabbableElementInArray;
  // true if user opens modal via keypress
  let keyInput = false;
  document.addEventListener('keydown', (e) => {
    if (e.key == 'Enter' || e.key == ' ' || e.key == 'Escape') keyInput = true;
  });
  
  function _setTabindex(el, val) {
    [...el.querySelectorAll(getAllTabbableElements)].forEach(element => {
      element.setAttribute('tabindex', val);
    });
  }
  
  function _setFocusOnFirstOrLastElement(e) {
    // Focus on last item if shift+tab is pressed and focus is on the first
    if (e.shiftKey && e.key == 'Tab' && tabbableElementsArray.indexOf(document.activeElement) === 0) {
      tabbableElementsArray[lastTabbableElementInArray].focus()
      e.preventDefault()
    }
  
    // Focus on first item if tab(9) is pressed and focus is on the last
    if (!e.shiftKey && e.key == 'Tab' && tabbableElementsArray.indexOf(document.activeElement) === lastTabbableElementInArray) {
      tabbableElementsArray[0].focus()
      e.preventDefault()
    }
  }
  
  function makeElementsUntabbable(el) {
    _setTabindex(el, -1);
  }
  
  function trapTabWithinPopup(el) {
    tabbableElementsArray = new Array(...el.querySelectorAll(getAllTabbableElements));
    lastTabbableElementInArray = tabbableElementsArray.length - 1;
  
    // Focuses on element if click to open
    // Focuses on close if key press to open
    keyInput ? tabbableElementsArray[0].focus() : el.focus();
    keyInput = false;
  
    document.addEventListener('keydown', _setFocusOnFirstOrLastElement);
  }
  
  function makeElementsTabbable(el) {
    _setTabindex(el, 0);
  }
  
  function makeElementsUntabbableAndFocusOnTrigger(el, button) {
    _setTabindex(el, -1);
    keyInput ? button.focus() : '';
    
    document.removeEventListener('keydown', _setFocusOnFirstOrLastElement);
    keyInput = false;
  }
  
  
  
  // Component Init
  const modal = new Modal(document.querySelector('[data-module="modal"]'))