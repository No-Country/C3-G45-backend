import Footer from '../footer/Footer';
import Navbar from '../nav/Navbar';
import PrincipalSection from '../principal/PrincipalSection';
import './App.css';

function App() {
  return (
    <>
      <div className="App">
        <Navbar />
          <PrincipalSection />
        <Footer />
      </div>
    </>
  );
}

export default App;
