import playerComparison from './views/playerComparison'
import Home from './components/Home'
import Monitor from "./views/Monitor"

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
      },
      {
        name: "Monitor",
        path: "/monitor",
        component: Monitor
      }
]