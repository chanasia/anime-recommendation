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
        'inputText-color': '#555'
      },
      borderColor: {
        'main-color': '#ed1ef5',
        'inputText-color': '#555'
      }
    },
  },
  variants: {
    borderColor: ['focus']
  },
  plugins: [],
}
