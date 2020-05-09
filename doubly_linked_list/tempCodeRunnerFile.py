  self.dll.delete(self.dll.head)
        self.assertEqual(self.dll.head.value, 6)
        self.assertEqual(self.dll.tail.value, 6)
        self