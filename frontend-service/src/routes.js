import playerComparison from './views/playerComparison'
import Home from './components/Home'

export default [
    {
        name: 'Player comparison',
        path: '/playercomparison',
        component: playerComparison
      },
      {
        name: 'Home',
        path: '/',
        component: Home
      }
]