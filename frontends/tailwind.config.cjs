/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors:{
        'main-color': '#ed1ef5',
        'font-color': '#efef',
        'inputText-color': '#555'
      },
      backgroundColor:{
        'main-color': '#ed1ef5',
        'background-color': '#373a3c',
        'inputText-color': '#555',
        'inputText2-color': '#333'
      },
      borderColor: {
        'main-color': '#ed1ef5',
        'inputText-color': '#555'
      },
      gridTemplateColumns:{
        'currentAnime': '1fr 2fr',
        'labelInfo': '100px 1fr'
      },
      width: {
        '128': '32rem',
        '160': '40rem',
        '192': '48rem'
      }
    },
  },
  variants: {
    borderColor: ['focus']
  },
  plugins: [],
}
