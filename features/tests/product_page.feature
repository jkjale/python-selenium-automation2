Feature: Product page functionality

  Scenario Outline: User can select all color options of a product
    Given Open Target product <product_id> page
    Then Click and verify colors starting at color index <color_ind> and labels list index <labels_list_ind>
    Examples:
      | product_id | color_ind | labels_list_ind |
      | A-54551690 | 0         | 0               |
      | A-91511634 | 12        | 1               |