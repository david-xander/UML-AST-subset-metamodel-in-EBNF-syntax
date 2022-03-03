from textx import metamodel_from_file
import unittest


class BaseMixin(unittest.TestCase):
    def create_data(self) -> None:
        meta_model = metamodel_from_file("uml.tx")
        self.cars = meta_model.model_from_file("cars.model")
        self.company = meta_model.model_from_file("company.model")
        self.graph = meta_model.model_from_file("graph.model")


class AcceptanceTestCase(BaseMixin):

    def setUp(self) -> None:
        self.create_data()

    def test_model_name(self):
        self.assertEqual("Cars", self.cars.model)

    def test_model_number_of_classes(self):
        self.assertEqual(2, len(self.cars.classes))

    def test_model_attributes_primitives(self):
        self.assertEqual("brand", self.cars.classes[0].attributes.attribute[0].name)
        self.assertEqual("String", self.cars.classes[0].attributes.attribute[0].type)
        self.assertEqual("color", self.cars.classes[0].attributes.attribute[1].name)
        self.assertEqual("String", self.cars.classes[0].attributes.attribute[1].type)

    def test_model_operations(self):
        self.assertEqual("increaseMileage", self.cars.classes[0].operations.operation[0].name)
        self.assertEqual("kilometers", self.cars.classes[0].operations.operation[0].variables[0].name)
        self.assertEqual("Integer", self.cars.classes[0].operations.operation[0].variables[0].type)

    def test_model_associations(self):
        self.assertEqual("Owner", self.cars.associations[0].name)
        self.assertEqual("Person", self.cars.associations[0].associate[0].name)
        self.assertEqual("hasA", self.cars.associations[0].associate[0].role)
        self.assertEqual("Car", self.cars.associations[0].associate[1].name)
        self.assertEqual("isOwnedBy", self.cars.associations[0].associate[1].role)
    
    def test_model_associations_multiplicity(self):
        self.assertEqual("1", self.cars.associations[0].associate[0].multiplicity)
        self.assertEqual("0..1", self.cars.associations[0].associate[1].multiplicity)
        self.assertEqual("*", self.graph.associations[0].associate[1].multiplicity)
        self.assertEqual("*", self.graph.associations[0].associate[1].multiplicity)




    def tearDown(self) -> None:
        super().tearDown()


if __name__ == '__main__':
    unittest.main()  # pragma: no cover