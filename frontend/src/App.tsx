import ListGroup from "./components/ListGroup";
import Login from "./components/Login";

function App() {
  let items = ["Beograd", "Novi Sad", "Subotica", "Kragujevac", "Uzice"];

  const handleSelectItem = (item: string) => {
    console.log(item);
  };
  return (
    <div>
      <Login></Login>
      <ListGroup
        items={items}
        heading="Cities"
        onSelectItem={handleSelectItem}
      ></ListGroup>
    </div>
  );
}

export default App;
