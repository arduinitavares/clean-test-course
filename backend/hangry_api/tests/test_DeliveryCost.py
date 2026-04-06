from api.controllers import Delivery
from django_mock_queries.query import MockModel, MockSet


def test_LotsOfItems():
    # Arrange
    order = MockSet()
    order.add(MockModel(quantity=5))
    order.add(MockModel(quantity=5))
    order.add(MockModel(quantity=5))
    delivery_distance = 6
    # Act
    cost = Delivery.calculate(order, delivery_distance)
    # Assert
    assert cost == 7.5


def test_MiddleOfTheRoadItems():
    # Arrange
    order = MockSet()
    order.add(MockModel(quantity=2))
    order.add(MockModel(quantity=2))
    order.add(MockModel(quantity=2))
    delivery_distance = 4
    # Act
    cost = Delivery.calculate(order, delivery_distance)
    # Assert
    assert cost == 5


def test_LittleItems():
    """Check the cost of delivery for a small order.

    This test checks the cost of delivery when there are only a few
    items in the order.
    """
    # Arrange
    order: MockSet = MockSet()
    order.add(MockModel(quantity=3))
    order.add(MockModel(quantity=1))
    delivery_distance = 2
    # Act
    # Call the function that will be tested
    cost: float = Delivery.calculate(order, delivery_distance)

    # Assert
    # replace the pass with an assert to test the value returned.
    assert cost == 2.5
