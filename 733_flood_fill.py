class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        if image[sr][sc] == color:
            return image
        starting_color = image[sr][sc]
        image[sr][sc] = color
        if sr - 1 >= 0 and image[sr - 1][sc] == starting_color:
            image = self.floodFill(image, sr - 1, sc, color)
        if sr + 1 < len(image) and image[sr + 1][sc] == starting_color:
            image = self.floodFill(image, sr + 1, sc, color)
        if sc - 1 >= 0 and image[sr][sc - 1] == starting_color:
            image = self.floodFill(image, sr, sc - 1, color)
        if sc + 1 < len(image[sr]) and image[sr][sc + 1] == starting_color:
            image = self.floodFill(image, sr, sc + 1, color)
        return image


if __name__ == "__main__":
    s = Solution()
    assert s.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [
        [2, 2, 2],
        [2, 2, 0],
        [2, 0, 1],
    ]
